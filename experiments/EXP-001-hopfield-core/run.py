from __future__ import annotations

import json
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np


EXPERIMENT_ID = "EXP-001"
N = 100
P = 3
PATTERN_SEED = 1982
NOISE_FRACTION = 0.20
TRIALS_PER_PATTERN = 50
MAX_SWEEPS = 50
ENERGY_TOLERANCE = 1e-10
RECOVERY_PASS_RATE = 0.95

RESULTS_DIR = Path(__file__).resolve().parent / "results"
SUMMARY_PATH = RESULTS_DIR / "summary.json"
TRIALS_PATH = RESULTS_DIR / "trials.jsonl"


@dataclass
class TrialResult:
    pattern_index: int
    trial_index: int
    corruption_seed: int
    update_seed: int
    flipped_bits: int
    recovered_exactly: bool
    converged: bool
    sweeps: int
    state_changes: int
    energy_increase_count: int
    max_positive_energy_delta: float
    initial_energy: float
    tracked_final_energy: float
    recomputed_final_energy: float
    energy_crosscheck_error: float


def make_patterns() -> np.ndarray:
    rng = np.random.default_rng(PATTERN_SEED)
    return rng.choice(np.array([-1, 1], dtype=np.int8), size=(P, N))


def build_weights(patterns: np.ndarray) -> np.ndarray:
    weights = (patterns.T @ patterns).astype(np.float64) / N
    np.fill_diagonal(weights, 0.0)
    return weights


def energy(state: np.ndarray, weights: np.ndarray) -> float:
    return float(-0.5 * state @ weights @ state)


def updated_value(local_field: float, current: int) -> int:
    if local_field > 0.0:
        return 1
    if local_field < 0.0:
        return -1
    return int(current)


def is_fixed_point(pattern: np.ndarray, weights: np.ndarray) -> bool:
    local_fields = weights @ pattern
    updated = np.array(
        [updated_value(float(h), int(x)) for h, x in zip(local_fields, pattern)],
        dtype=np.int8,
    )
    return bool(np.array_equal(updated, pattern))


def corrupt_pattern(pattern: np.ndarray, seed: int) -> tuple[np.ndarray, int]:
    rng = np.random.default_rng(seed)
    corrupted = pattern.copy()
    flip_count = int(round(N * NOISE_FRACTION))
    indices = rng.choice(N, size=flip_count, replace=False)
    corrupted[indices] *= -1
    return corrupted, flip_count


def run_trial(
    target: np.ndarray,
    pattern_index: int,
    trial_index: int,
    weights: np.ndarray,
) -> TrialResult:
    corruption_seed = 100000 + pattern_index * 1000 + trial_index
    update_seed = 200000 + pattern_index * 1000 + trial_index

    state, flipped_bits = corrupt_pattern(target, corruption_seed)
    rng = np.random.default_rng(update_seed)

    tracked_energy = energy(state, weights)
    initial_energy = tracked_energy
    energy_increase_count = 0
    max_positive_energy_delta = 0.0
    state_changes = 0
    converged = False
    sweeps_completed = 0

    for sweep in range(1, MAX_SWEEPS + 1):
        changes_this_sweep = 0

        for neuron_index in rng.permutation(N):
            old_value = int(state[neuron_index])
            local_field = float(weights[neuron_index] @ state)
            new_value = updated_value(local_field, old_value)

            if new_value == old_value:
                continue

            # For symmetric weights with zero diagonal, changing one neuron gives:
            # ΔE = -(x'_i - x_i) h_i
            delta_energy = -float(new_value - old_value) * local_field
            tracked_energy += delta_energy

            if delta_energy > ENERGY_TOLERANCE:
                energy_increase_count += 1
                max_positive_energy_delta = max(max_positive_energy_delta, delta_energy)

            state[neuron_index] = new_value
            changes_this_sweep += 1
            state_changes += 1

        sweeps_completed = sweep
        if changes_this_sweep == 0:
            converged = True
            break

    recomputed_final_energy = energy(state, weights)
    crosscheck_error = abs(tracked_energy - recomputed_final_energy)

    return TrialResult(
        pattern_index=pattern_index,
        trial_index=trial_index,
        corruption_seed=corruption_seed,
        update_seed=update_seed,
        flipped_bits=flipped_bits,
        recovered_exactly=bool(np.array_equal(state, target)),
        converged=converged,
        sweeps=sweeps_completed,
        state_changes=state_changes,
        energy_increase_count=energy_increase_count,
        max_positive_energy_delta=max_positive_energy_delta,
        initial_energy=initial_energy,
        tracked_final_energy=tracked_energy,
        recomputed_final_energy=recomputed_final_energy,
        energy_crosscheck_error=crosscheck_error,
    )


def main() -> None:
    patterns = make_patterns()
    weights = build_weights(patterns)

    symmetric_weights = bool(np.allclose(weights, weights.T, atol=0.0, rtol=0.0))
    zero_diagonal = bool(np.allclose(np.diag(weights), 0.0, atol=0.0, rtol=0.0))
    fixed_points = [is_fixed_point(pattern, weights) for pattern in patterns]

    trials: list[TrialResult] = []
    for pattern_index, target in enumerate(patterns):
        for trial_index in range(TRIALS_PER_PATTERN):
            trials.append(
                run_trial(
                    target=target,
                    pattern_index=pattern_index,
                    trial_index=trial_index,
                    weights=weights,
                )
            )

    total_trials = len(trials)
    recovered = sum(t.recovered_exactly for t in trials)
    recovery_rate = recovered / total_trials
    all_converged = all(t.converged for t in trials)
    total_energy_increases = sum(t.energy_increase_count for t in trials)
    max_positive_delta = max(t.max_positive_energy_delta for t in trials)
    max_energy_crosscheck_error = max(t.energy_crosscheck_error for t in trials)

    per_pattern = []
    for pattern_index in range(P):
        pattern_trials = [t for t in trials if t.pattern_index == pattern_index]
        successes = sum(t.recovered_exactly for t in pattern_trials)
        per_pattern.append(
            {
                "pattern_index": pattern_index,
                "successes": successes,
                "trials": len(pattern_trials),
                "recovery_rate": successes / len(pattern_trials),
            }
        )

    pass_conditions = {
        "all_stored_patterns_are_fixed_points": all(fixed_points),
        "recovery_rate_at_least_0_95": recovery_rate >= RECOVERY_PASS_RATE,
        "zero_energy_increases_above_tolerance": total_energy_increases == 0,
        "all_trials_converged_within_50_sweeps": all_converged,
    }

    decision = "PASS" if all(pass_conditions.values()) else "FAIL"

    summary = {
        "experiment_id": EXPERIMENT_ID,
        "decision": decision,
        "config": {
            "N": N,
            "P": P,
            "pattern_seed": PATTERN_SEED,
            "noise_fraction": NOISE_FRACTION,
            "trials_per_pattern": TRIALS_PER_PATTERN,
            "total_trials": total_trials,
            "max_sweeps": MAX_SWEEPS,
            "energy_tolerance": ENERGY_TOLERANCE,
            "recovery_pass_rate": RECOVERY_PASS_RATE,
        },
        "environment": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "weight_checks": {
            "symmetric": symmetric_weights,
            "zero_diagonal": zero_diagonal,
        },
        "fixed_points": fixed_points,
        "metrics": {
            "recovered": recovered,
            "recovery_rate": recovery_rate,
            "all_converged": all_converged,
            "total_energy_increases": total_energy_increases,
            "max_positive_energy_delta": max_positive_delta,
            "max_energy_crosscheck_error": max_energy_crosscheck_error,
            "max_sweeps_observed": max(t.sweeps for t in trials),
            "total_state_changes": sum(t.state_changes for t in trials),
        },
        "per_pattern": per_pattern,
        "pass_conditions": pass_conditions,
        "notes": [
            "PASS/FAIL is the pre-registered decision for EXP-001, not a truth value for H-001.",
            "The 20% corruption and 95% recovery threshold are project-defined operational criteria, not claimed as numeric thresholds from Hopfield (1982).",
            "Energy is a dimensionless Lyapunov quantity, not physical energy in joules.",
        ],
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    with TRIALS_PATH.open("w", encoding="utf-8") as handle:
        for trial in trials:
            handle.write(json.dumps(asdict(trial), ensure_ascii=False) + "\n")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"\nWrote: {SUMMARY_PATH}")
    print(f"Wrote: {TRIALS_PATH}")


if __name__ == "__main__":
    main()

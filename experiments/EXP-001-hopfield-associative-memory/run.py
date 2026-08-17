from __future__ import annotations

import csv
import json
import platform
import sys
from pathlib import Path

import numpy as np

N = 100
P = 5
PATTERN_SEED = 1982
NOISE_RATES = (0.10, 0.20)
TRIALS_PER_PATTERN = 20
MAX_SWEEPS = 20

PASS_THRESHOLDS = {
    0.10: 0.95,
    0.20: 0.80,
}


def build_patterns() -> np.ndarray:
    rng = np.random.default_rng(PATTERN_SEED)
    return rng.choice(np.array([-1, 1], dtype=np.int8), size=(P, N), replace=True)


def build_weights(patterns: np.ndarray) -> np.ndarray:
    weights = (patterns.T @ patterns).astype(np.float64) / N
    np.fill_diagonal(weights, 0.0)
    return weights


def make_trial_seed(noise_index: int, pattern_index: int, trial_index: int) -> int:
    return (
        PATTERN_SEED
        + (noise_index + 1) * 1_000_000
        + (pattern_index + 1) * 10_000
        + trial_index
    )


def corrupt(pattern: np.ndarray, noise_rate: float, rng: np.random.Generator) -> np.ndarray:
    state = pattern.copy()
    flip_count = int(round(noise_rate * N))
    indices = rng.choice(N, size=flip_count, replace=False)
    state[indices] *= -1
    return state


def recall(
    initial_state: np.ndarray,
    weights: np.ndarray,
    rng: np.random.Generator,
) -> tuple[np.ndarray, bool, int]:
    state = initial_state.copy()

    for sweep in range(1, MAX_SWEEPS + 1):
        changed = 0
        for i in rng.permutation(N):
            local_field = float(weights[i] @ state)
            if local_field > 0:
                new_value = 1
            elif local_field < 0:
                new_value = -1
            else:
                new_value = int(state[i])

            if new_value != state[i]:
                state[i] = new_value
                changed += 1

        if changed == 0:
            return state, True, sweep

    return state, False, MAX_SWEEPS


def hamming_distance(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.count_nonzero(a != b))


def write_patterns(path: Path, patterns: np.ndarray) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["pattern_index", *[f"bit_{i}" for i in range(N)]])
        for pattern_index, pattern in enumerate(patterns):
            writer.writerow([pattern_index, *pattern.tolist()])


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    results_dir = base_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    patterns = build_patterns()
    weights = build_weights(patterns)
    write_patterns(results_dir / "patterns.csv", patterns)

    trial_rows: list[dict[str, object]] = []

    for noise_index, noise_rate in enumerate(NOISE_RATES):
        for pattern_index, target in enumerate(patterns):
            for trial_index in range(TRIALS_PER_PATTERN):
                seed = make_trial_seed(noise_index, pattern_index, trial_index)
                rng = np.random.default_rng(seed)
                initial = corrupt(target, noise_rate, rng)
                recalled, converged, sweeps = recall(initial, weights, rng)

                trial_rows.append(
                    {
                        "noise_rate": noise_rate,
                        "pattern_index": pattern_index,
                        "trial_index": trial_index,
                        "trial_seed": seed,
                        "initial_hamming_distance": hamming_distance(initial, target),
                        "final_hamming_distance": hamming_distance(recalled, target),
                        "exact_recall": bool(np.array_equal(recalled, target)),
                        "converged": converged,
                        "sweeps": sweeps,
                    }
                )

    trials_path = results_dir / "trials.csv"
    with trials_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = list(trial_rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(trial_rows)

    per_noise: dict[str, dict[str, float | int]] = {}
    for noise_rate in NOISE_RATES:
        rows = [row for row in trial_rows if row["noise_rate"] == noise_rate]
        total = len(rows)
        exact_count = sum(bool(row["exact_recall"]) for row in rows)
        converged_count = sum(bool(row["converged"]) for row in rows)
        mean_sweeps = sum(int(row["sweeps"]) for row in rows) / total
        mean_initial_distance = (
            sum(int(row["initial_hamming_distance"]) for row in rows) / total
        )
        mean_final_distance = (
            sum(int(row["final_hamming_distance"]) for row in rows) / total
        )

        per_noise[f"{noise_rate:.2f}"] = {
            "trials": total,
            "exact_recall_count": exact_count,
            "exact_recall_rate": exact_count / total,
            "converged_count": converged_count,
            "convergence_rate": converged_count / total,
            "mean_sweeps": mean_sweeps,
            "mean_initial_hamming_distance": mean_initial_distance,
            "mean_final_hamming_distance": mean_final_distance,
        }

    expected_trial_count = len(NOISE_RATES) * P * TRIALS_PER_PATTERN
    valid_trial_count = len(trial_rows)
    pass_conditions = {
        f"{noise_rate:.2f}": per_noise[f"{noise_rate:.2f}"]["exact_recall_rate"]
        >= threshold
        for noise_rate, threshold in PASS_THRESHOLDS.items()
    }

    decision = (
        "PASS"
        if valid_trial_count == expected_trial_count and all(pass_conditions.values())
        else "FAIL"
    )

    summary = {
        "experiment_id": "EXP-001",
        "status": "executed",
        "decision": decision,
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "config": {
            "N": N,
            "P": P,
            "load": P / N,
            "pattern_seed": PATTERN_SEED,
            "noise_rates": list(NOISE_RATES),
            "trials_per_pattern": TRIALS_PER_PATTERN,
            "max_sweeps": MAX_SWEEPS,
            "update": "asynchronous shuffled order per sweep",
            "weight_rule": "Hebbian outer-product, diagonal zero",
        },
        "expected_trial_count": expected_trial_count,
        "valid_trial_count": valid_trial_count,
        "pass_thresholds": {f"{k:.2f}": v for k, v in PASS_THRESHOLDS.items()},
        "pass_conditions": pass_conditions,
        "per_noise": per_noise,
        "note": (
            "Script-level PASS/FAIL assumes the run followed the preregistered code and conditions. "
            "Repository interpretation may be set to UNCERTAIN if implementation or raw-output "
            "validation reveals a problem."
        ),
    }

    summary_path = results_dir / "summary.json"
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

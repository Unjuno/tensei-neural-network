from __future__ import annotations

import itertools
import json
import platform
import sys
from collections import Counter
from pathlib import Path

import numpy as np

N = 100
P_VALUES = (5, 10, 15, 20)
NOISE_RATES = (0.10, 0.20, 0.30, 0.40)
PATTERN_SEEDS = (1982, 1983, 1984)
TRIALS_PER_CONDITION = 20
MAX_SWEEPS = 20
EXPECTED_TOTAL = 960
EXPECTED_NONSTORED = 510


def generate_max_patterns(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.choice(np.array([-1, 1], dtype=np.int8), size=(max(P_VALUES), N), replace=True)


def build_weights(patterns: np.ndarray) -> np.ndarray:
    weights = (patterns.T @ patterns).astype(np.float64) / N
    np.fill_diagonal(weights, 0.0)
    return weights


def trial_seed(seed_index: int, p_index: int, noise_index: int, trial_index: int) -> int:
    return 2_002_000 + seed_index * 1_000_000 + p_index * 100_000 + noise_index * 1_000 + trial_index


def corrupt(pattern: np.ndarray, noise_rate: float, rng: np.random.Generator) -> np.ndarray:
    state = pattern.copy()
    flip_count = int(round(noise_rate * N))
    flip_indices = rng.choice(N, size=flip_count, replace=False)
    state[flip_indices] *= -1
    return state


def recall(initial_state: np.ndarray, weights: np.ndarray, rng: np.random.Generator) -> tuple[np.ndarray, bool, int]:
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


def classify_final(final_state: np.ndarray, target_index: int, stored_patterns: np.ndarray, converged: bool) -> str:
    stored_distances = np.count_nonzero(stored_patterns != final_state, axis=1)
    if stored_distances[target_index] == 0:
        return "TARGET_EXACT"
    if np.any(stored_distances == 0):
        return "WRONG_STORED"
    if converged:
        return "NONSTORED_CONVERGED"
    return "NONCONVERGED"


def three_pattern_candidates(patterns: np.ndarray) -> list[tuple[tuple[int, int, int], int, np.ndarray]]:
    candidates: list[tuple[tuple[int, int, int], int, np.ndarray]] = []
    for combo in itertools.combinations(range(len(patterns)), 3):
        summed = patterns[list(combo)].sum(axis=0)
        mixture = np.where(summed > 0, 1, -1).astype(np.int8)
        candidates.append((combo, 1, mixture))
        candidates.append((combo, -1, -mixture))
    return candidates


def main() -> None:
    rows: list[dict[str, object]] = []
    exact_matches: list[dict[str, object]] = []

    for seed_index, pattern_seed in enumerate(PATTERN_SEEDS):
        max_patterns = generate_max_patterns(pattern_seed)
        for p_index, p in enumerate(P_VALUES):
            patterns = max_patterns[:p]
            weights = build_weights(patterns)
            candidates = three_pattern_candidates(patterns)

            for noise_index, noise_rate in enumerate(NOISE_RATES):
                for trial_index in range(TRIALS_PER_CONDITION):
                    target_index = (trial_index + seed_index * 7) % p
                    target = patterns[target_index]
                    seed = trial_seed(seed_index, p_index, noise_index, trial_index)
                    rng = np.random.default_rng(seed)
                    initial = corrupt(target, noise_rate, rng)
                    final_state, converged, sweeps = recall(initial, weights, rng)
                    category = classify_final(final_state, target_index, patterns, converged)

                    row = {
                        "pattern_seed": pattern_seed,
                        "P": p,
                        "noise_rate": noise_rate,
                        "trial_index": trial_index,
                        "target_index": target_index,
                        "trial_seed": seed,
                        "final_category": category,
                        "sweeps": sweeps,
                    }
                    rows.append(row)

                    if category != "NONSTORED_CONVERGED":
                        continue

                    nearest_stored = int(np.count_nonzero(patterns != final_state, axis=1).min())
                    nearest_mixture = N + 1
                    matches: list[tuple[tuple[int, int, int], int]] = []
                    for combo, sign, candidate in candidates:
                        distance = int(np.count_nonzero(candidate != final_state))
                        nearest_mixture = min(nearest_mixture, distance)
                        if distance == 0:
                            matches.append((combo, sign))

                    if matches:
                        exact_matches.append(
                            {
                                **row,
                                "nearest_stored_hamming": nearest_stored,
                                "nearest_mixture_hamming": nearest_mixture,
                                "matches": [
                                    {"patterns": list(combo), "sign": sign}
                                    for combo, sign in matches
                                ],
                            }
                        )

                    row["nearest_stored_hamming"] = nearest_stored
                    row["nearest_mixture_hamming"] = nearest_mixture

    counts = Counter(str(row["final_category"]) for row in rows)
    valid_total = len(rows)
    nonstored_count = counts["NONSTORED_CONVERGED"]
    exact_match_count = len(exact_matches)

    regeneration_valid = valid_total == EXPECTED_TOTAL and nonstored_count == EXPECTED_NONSTORED
    if not regeneration_valid:
        decision = "UNCERTAIN"
    elif exact_match_count >= 1:
        decision = "PASS"
    else:
        decision = "FAIL"

    nonstored_rows = [row for row in rows if row["final_category"] == "NONSTORED_CONVERGED"]
    closer_to_mixture = sum(
        int(row["nearest_mixture_hamming"]) < int(row["nearest_stored_hamming"])
        for row in nonstored_rows
    )

    summary = {
        "experiment_id": "EXP-003",
        "status": "executed",
        "decision": decision,
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "regeneration": {
            "expected_total_trials": EXPECTED_TOTAL,
            "observed_total_trials": valid_total,
            "expected_nonstored_converged": EXPECTED_NONSTORED,
            "observed_nonstored_converged": nonstored_count,
            "valid": regeneration_valid,
            "category_counts": dict(counts),
        },
        "pre_registered_result": {
            "exact_three_pattern_mixture_match_trials": exact_match_count,
            "pass_condition": "at least one exact match among 510 NONSTORED_CONVERGED states",
        },
        "exploratory": {
            "nonstored_states_closer_to_three_pattern_mixture_than_any_stored_pattern": closer_to_mixture,
            "fraction_closer_to_mixture": closer_to_mixture / nonstored_count if nonstored_count else None,
        },
        "exact_matches": exact_matches,
        "note": "Exact 3-pattern majority-mixture matching is a narrow structural test; it does not classify all spurious attractors.",
    }

    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

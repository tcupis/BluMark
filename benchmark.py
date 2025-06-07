"""CPU benchmarking utilities."""

import csv
import os
import platform
from datetime import datetime
import time


class Benchmark:
    """Run a series of CPU bound tests and record the results."""

    METRIC_KEYS = [
        "fpc_ops",
        "fpa_ops",
        "fpm_ops",
        "fpd_ops",
        "brs_ops",
        "brm_ops",
    ]
    HEADERS = [
        "timestamp",
        "node",
        "system",
        "machine",
    ] + METRIC_KEYS

    def __init__(self, csv_file: str = "results.csv"):
        self.csv_file = csv_file

    def _measure(self, func, iterations: int) -> float:
        start = time.perf_counter()
        func(iterations)
        elapsed = time.perf_counter() - start
        return iterations / elapsed

    def _run_trials(self, func, iterations: int, trials: int) -> float:
        total = 0.0
        for _ in range(trials):
            total += self._measure(func, iterations)
        return total / trials

    @staticmethod
    def _loop_add(iterations: int) -> None:
        x = 0.0
        for _ in range(iterations):
            x += 1.0

    @staticmethod
    def _loop_sub(iterations: int) -> None:
        x = 0.0
        for _ in range(iterations):
            x -= 1.0

    @staticmethod
    def _loop_mul(iterations: int) -> None:
        x = 1.0
        for _ in range(iterations):
            x *= 1.000001

    @staticmethod
    def _loop_div(iterations: int) -> None:
        x = 1.0
        for _ in range(iterations):
            x /= 1.000001

    @staticmethod
    def _branch_simple(iterations: int) -> None:
        x = 0
        for i in range(iterations):
            if i % 2:
                x += 1
            else:
                x -= 1

    @staticmethod
    def _branch_mixed(iterations: int) -> None:
        x = 0
        for i in range(iterations):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                x -= 1
            else:
                x += 2

    def run(self, iterations: int = 1_000_000, trials: int = 3):
        """Execute the benchmark and return operations per second for each test."""
        results = {
            "fpc_ops": self._run_trials(self._loop_add, iterations, trials),
            "fpa_ops": self._run_trials(self._loop_sub, iterations, trials),
            "fpm_ops": self._run_trials(self._loop_mul, iterations, trials),
            "fpd_ops": self._run_trials(self._loop_div, iterations, trials),
            "brs_ops": self._run_trials(self._branch_simple, iterations, trials),
            "brm_ops": self._run_trials(self._branch_mixed, iterations, trials),
        }

        self._write_results(results)
        return results

    def _write_results(self, results):
        first = not os.path.exists(self.csv_file)
        row = {
            "timestamp": datetime.now().isoformat(sep=" ", timespec="seconds"),
            "node": platform.node(),
            "system": platform.system(),
            "machine": platform.machine(),
        }
        row.update(results)
        with open(self.csv_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADERS)
            if first:
                writer.writeheader()
            writer.writerow(row)

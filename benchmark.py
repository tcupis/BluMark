import csv
import os
import random
import time


class Benchmark:
    HEADERS = [
        "fpc_score",
        "fpa_score",
        "fpm_score",
        "fpd_score",
        "brs_score",
        "brm_score",
    ]

    def __init__(self, csv_file="results.csv"):
        self.csv_file = csv_file

    def run(self, duration=0.5):
        results = {key: 0 for key in self.HEADERS}

        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            results["fpc_score"] += 1

        temp = 0.0
        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            temp += random.random()
            results["fpa_score"] += 1

        temp = 1.0
        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            temp *= random.random()
            results["fpm_score"] += 1

        temp = 1.0
        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            rnd = random.random() or 1e-9
            temp /= rnd
            results["fpd_score"] += 1

        temp = 0.0
        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            if random.random() > 0.5:
                temp += 1
            else:
                temp -= 1
            results["brs_score"] += 1

        end = time.perf_counter() + duration
        while time.perf_counter() < end:
            tmp = random.random()
            if tmp > 0.75:
                tmp += 1
            elif tmp > 0.5:
                tmp -= 1
            elif tmp > 0.25:
                tmp += 1
            else:
                tmp -= 1
            results["brm_score"] += 1

        self._write_results(results)
        return results

    def _write_results(self, results):
        first = not os.path.exists(self.csv_file)
        with open(self.csv_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADERS)
            if first:
                writer.writeheader()
            writer.writerow(results)

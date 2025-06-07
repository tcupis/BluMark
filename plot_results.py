import csv
import sys
import matplotlib.pyplot as plt


def plot_results(csv_file="results.csv"):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        runs = [ {k: int(v) for k, v in row.items()} for row in reader ]

    if not runs:
        print("No results found.")
        return

    headers = list(runs[0].keys())
    x = list(range(1, len(runs) + 1))

    for header in headers:
        plt.figure()
        plt.plot(x, [run[header] for run in runs], marker="o")
        plt.title(header)
        plt.xlabel("Run")
        plt.ylabel("Count")
        plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "results.csv"
    plot_results(csv_file)

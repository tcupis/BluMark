import csv
import os
import platform
import tkinter as tk
import threading
from benchmark import Benchmark
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.title("BluMark")
        self.root.configure(bg="#242424")

        self.score_label = tk.Label(
            self.root,
            text="0.0",
            bg="#1e90ff",
            fg="white",
            font=("Helvetica", 40, "bold"),
        )
        self.score_label.pack(pady=20, ipadx=40)

        self.status_label = tk.Label(
            self.root, text="Ready", bg="#242424", fg="white", font=("Helvetica", 12)
        )
        self.status_label.pack(pady=(0, 10))

        self.run_button = tk.Button(
            self.root,
            text="Run Benchmark",
            command=self.run,
            bg="#4caf50",
            fg="white",
            activebackground="#45a049",
            relief=tk.FLAT,
            font=("Helvetica", 14, "bold"),
            width=15,
        )
        self.run_button.pack(ipady=8)

        self.history_button = tk.Button(
            self.root,
            text="Show History",
            command=self.show_history,
            bg="#2196f3",
            fg="white",
            activebackground="#1976d2",
            relief=tk.FLAT,
            font=("Helvetica", 12, "bold"),
            width=15,
        )
        self.history_button.pack(pady=(10, 0), ipady=4)

        self.graph_frame = tk.Frame(self.root, bg="#242424")
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.canvas = None

        self.benchmark = Benchmark()
        self.running = False

    def run(self):
        if self.running:
            return
        self.running = True
        self.run_button.config(state=tk.DISABLED)
        self.status_label.config(text="Running...")
        threading.Thread(target=self._run_benchmark, daemon=True).start()

    def _run_benchmark(self):
        results = self.benchmark.run()
        total = sum(results.values()) / 100000
        self.score_label.config(text=f"{total:.1f}")
        self.status_label.config(text="Done")
        self.run_button.config(state=tk.NORMAL)
        self.running = False

    def show_history(self):
        scores = self._load_scores()
        if not scores:
            return

        timestamps, totals = zip(*scores)

        fig = plt.Figure(figsize=(4, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(timestamps, totals, marker="o", color="#1e90ff")
        ax.set_title("History")
        ax.set_ylabel("Score")
        ax.tick_params(axis="x", rotation=45)
        fig.tight_layout()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _load_scores(self):
        if not os.path.exists(self.benchmark.csv_file):
            return []
        with open(self.benchmark.csv_file, newline="") as f:
            reader = csv.DictReader(f)
            scores = []
            for row in reader:
                if row.get("node") and row["node"] != platform.node():
                    continue
                try:
                    total = sum(
                        float(row[k]) for k in Benchmark.METRIC_KEYS if row.get(k)
                    )
                except (TypeError, ValueError):
                    # Skip malformed rows from older formats
                    continue
                ts = row.get("timestamp") or str(len(scores) + 1)
                scores.append((ts, total / 100000))
        return scores


if __name__ == "__main__":
    app = App()
    app.root.mainloop()

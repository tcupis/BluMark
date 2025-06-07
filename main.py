import tkinter as tk
import threading
from benchmark import Benchmark
import plot_results


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("240x160")
        self.root.title("BluMark")

        self.score_label = tk.Label(
            self.root, text="0", bg="lightblue", font=("Arial", 32, "bold")
        )
        self.score_label.pack(pady=10, ipadx=30)

        tk.Button(self.root, text="Run", command=self.run).pack(ipady=10, ipadx=70)
        tk.Button(self.root, text="Show Graphs", command=self.plot).pack(
            ipady=5, ipadx=60, pady=5
        )

        self.benchmark = Benchmark()

    def run(self):
        threading.Thread(target=self._run_benchmark).start()

    def _run_benchmark(self):
        results = self.benchmark.run()
        total = sum(results.values()) // 1000
        self.score_label.config(text=str(total))

    def plot(self):
        threading.Thread(target=plot_results.plot_results).start()


if __name__ == "__main__":
    app = App()
    app.root.mainloop()

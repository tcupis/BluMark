import tkinter as tk
import threading
from benchmark import Benchmark


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")
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


if __name__ == "__main__":
    app = App()
    app.root.mainloop()

import tkinter as tk
from tkinter import ttk
import threading
from benchmark import Benchmark


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x250")
        self.root.title("BluMark")
        self.root.configure(bg="#1e1e1e")

        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
        style.configure("Run.TButton", background="#4caf50", foreground="white")

        self.score_label = tk.Label(
            self.root,
            text="0.0",
            bg="#1e1e1e",
            fg="#00bfff",
            font=("Helvetica", 48, "bold"),
        )
        self.score_label.pack(pady=(20, 10))

        self.status_label = tk.Label(
            self.root, text="Ready", bg="#1e1e1e", fg="white", font=("Helvetica", 12)
        )
        self.status_label.pack()

        self.run_button = ttk.Button(
            self.root,
            text="Run Benchmark",
            command=self.run,
            style="Run.TButton",
            width=15,
        )
        self.run_button.pack(pady=(20, 0))


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

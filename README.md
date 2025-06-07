# BluMark

BluMark is a small CPU benchmark written in Python. It measures the speed of basic floating point and branching operations to give a rough indication of processor performance. The tests use deterministic loops and average multiple trials so the results are reasonably consistent. After each run a row is appended to `results.csv` containing the timestamp, machine details and operations-per-second metrics.

## Running

No extra packages are required. Launch the GUI with:

```bash
python main.py
```

Press **Run Benchmark** to execute the tests. The window shows the combined score in millions of operations per second. Detailed metrics are saved to `results.csv` for later inspection.

Open the CSV file in any spreadsheet or plotting tool to graph your scores over time.

## GUI
Screenshot of the application GUI after running a test on a AMD Ryzen 7 3700X 8-Core Processor giving it a score of `1.81`.

<img width="301" alt="GUI" src="https://github.com/user-attachments/assets/cd1c7d69-0d94-4a1c-b367-57c7af112b71" />



## Programmatic use

You can also invoke the benchmark from your own scripts:

```python
from benchmark import Benchmark

bench = Benchmark()
results = bench.run(iterations=1_000_000, trials=5)
print(results)
```

`results` is a dictionary mapping each metric name to the achieved operations per second.

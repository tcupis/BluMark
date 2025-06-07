# BluMark

BluMark is a lightweight benchmark for measuring CPU floating point and
branching performance. The tests run deterministic loops and average several
trials to produce reliable operations-per-second metrics. Each run records
results to `results.csv` along with the timestamp and machine information so you
can track performance over time.

## Usage

Install dependencies and run the GUI benchmark:

```bash
pip install matplotlib
python main.py
```

Press **Run** to execute the benchmark. The window displays a combined score in
millions of operations per second and the detailed metrics are appended to
`results.csv`.

Open `results.csv` in your spreadsheet or plotting tool of choice to track
results over time.

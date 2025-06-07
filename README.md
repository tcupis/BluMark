# BluMark

BluMark is a lightweight benchmark for measuring CPU floating point and branching
performance. Each run records results to `results.csv` so you can compare
performance over time.

## Usage

1. Install dependencies (only `matplotlib` is required for plotting):

```bash
pip install matplotlib
```

2. Run the GUI benchmark:

```bash
python main.py
```

Press **Run** to execute the benchmark. A score is shown in the window and the
raw counts are appended to `results.csv`.

3. To visualize how scores change across runs, execute:

```bash
python plot_results.py
```

This opens a set of graphs showing each metric for all recorded runs.

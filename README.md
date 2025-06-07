# BluMark

BluMark is a lightweight benchmark for measuring CPU floating point and branching
performance. Each run records results to `results.csv` so you can compare
performance over time.

## Usage

Run the GUI benchmark:

```bash
python main.py
```

Press **Run** to execute the benchmark. A score is shown in the window and the
raw counts are appended to `results.csv`.

The CSV file can be opened in your spreadsheet or plotting tool of choice to
track results over time.

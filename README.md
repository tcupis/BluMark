# BluMark

BluMark is a lightweight benchmark for measuring CPU floating point and branching
performance. Each run records results to `results.csv` so you can compare
performance over time. Every entry now includes the timestamp and basic details
about the machine that produced the score.

## Usage

Install dependencies and run the GUI benchmark:

```bash
pip install matplotlib
python main.py
```

Press **Run** to execute the benchmark. A score is shown in the window and the
raw counts are appended to `results.csv`.

Open `results.csv` in your spreadsheet or plotting tool of choice to track
results over time.

# Statistics Calculator

A pure Python CLI tool that implements core statistical functions from scratch — no NumPy, no external libraries.
Built to understand the math that powers machine learning, not just the function names.

---

## Features

- Mean, median, and mode from a raw list of numbers
- Population variance and standard deviation
- Pearson correlation coefficient between two datasets
- Min-max normalization (scales data to 0–1 range)
- Full summary report from a single input
- Test suite verifying every function against known values

---

## Project Structure

```
stats_calculator/
├── stats.py        # Pure math functions — no libraries
├── main.py         # CLI menu and user input
└── test.py         # Developer test suite
```

---

## Requirements

- Python 3.10 or higher
- No external dependencies

---

## Installation & Running

1. Clone or download this repository

2. Run the program:
```
python main.py
```

3. To run the test suite:
```
python test.py
```

---

## How to Use

On launch, a menu appears:

```
------------Menu------------
1. Summary of data set
2. Correlation of two data sets
q. Quit
```

### Summary (Option 1)

Enter a comma-separated list of numbers:
```
Data 1: 4, 8, 15, 16, 23, 42
```

Output:
```
----------Summary-------------

Mean:                18.000
Median:              15.5
Mode:                [4, 8, 15, 16, 23, 42]
Variance:            151.667
Standard Deviation:  12.315
Min Max:             [0.0, 0.10526, 0.28947, 0.31579, 0.5, 1.0]
```

### Correlation (Option 2)

Enter two comma-separated lists of equal length:
```
Data 1: 4, 8, 15, 16, 23, 42
Data 2: 1, 3, 6, 7, 9, 17

Correlation: 0.998
```

---

## The Math

Every function is implemented manually from its formula:

**Mean**
```
mean = sum(x) / n
```

**Variance** (population)
```
variance = sum((x - mean)²) / n
```

**Standard Deviation**
```
std = √variance
```

**Pearson Correlation**
```
r = covariance(x, y) / (std(x) * std(y))
```

**Min-Max Normalization**
```
normalized = (x - min) / (max - min)
```

---

## Test Suite

`test.py` verifies all 7 functions against pre-calculated values:

```
=== Running Tests ===
mean:        PASS
median even: PASS
median odd:  PASS
mode single: PASS
mode multi:  PASS
variance:    PASS
std_dev:     PASS
min_max:     PASS
correlation: PASS
```

Float comparisons use a tolerance of `0.001` to handle floating point precision.

---

## Why This Matters for ML

| Function | ML Application |
|---|---|
| `mean` | Centering data, computing loss |
| `std` | Z-score normalization |
| `variance` | What models minimize during training |
| `correlation` | Feature selection — correlated features add noise |
| `min_max` | Preprocessing before feeding data to neural networks |
| `mode` | Used in decision tree splitting |

---

## Notes

- All functions are pure — they return values without printing
- `min_max()` does not mutate the original list
- Mode returns a list — multiple values if there is a tie
- Correlation requires two lists of equal length

# Chennai Groundwater-Level Prediction

**Research title:** *Beyond Model Complexity: Feature-Engineered Machine Learning and Statistical Approaches for Monthly Groundwater-Level Prediction in Chennai, India.*

## Overview

This repository provides the Python source code and Jupyter Notebook used for the computational workflow described in the associated research manuscript. The workflow includes time-based feature engineering, machine-learning regression, LSTM modelling, hybrid prediction approaches, model evaluation, and visualization.

## Methods represented in the code

- Multiple Linear Regression (MLR)
- Support Vector Regression (SVR)
- Random Forest
- XGBoost
- LightGBM
- CatBoost
- Long Short-Term Memory (LSTM)
- LSTM–XGBoost hybrid
- LSTM–Random Forest–XGBoost hybrid
- Residual XGBoost–LSTM approach

## Repository contents

- `final_chennai_all.py` — Python implementation of the modelling workflow.
- `final_chennai_all.ipynb` — Jupyter/Google Colab notebook.
- `requirements.txt` — Python package dependencies.
- `example_test.py` — small synthetic-data smoke test for the Python environment and XGBoost installation.

## Data requirements

The full research dataset is not included in this repository. The main workflow expects an Excel file named `CHENNAI_Groundwater.xlsx` with, at minimum, the following columns:

- `Time` — monthly observation date/time.
- `Groundwater_Level_mbgl` — groundwater level in metres below ground level.

The script may use additional predictor columns where present, including `Rainfall_mm`. Users must have lawful access to the original dataset and should place it in the working directory or update `FILE_PATH` in the script.

## Installation

Use Python 3.10 or another version compatible with the listed packages.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Quick test

Run the synthetic-data smoke test:

```bash
python example_test.py
```

This test checks that the core scientific Python packages and XGBoost can be imported and that a small example regression model can be fitted. It does not reproduce the manuscript's numerical results.

## Run the research workflow

1. Obtain the authorized `CHENNAI_Groundwater.xlsx` input dataset.
2. Place it in the working directory.
3. Confirm that `FILE_PATH` in `final_chennai_all.py` points to the dataset.
4. Run:

```bash
python final_chennai_all.py
```

Alternatively, open `final_chennai_all.ipynb` in Jupyter Notebook or Google Colab and provide the input dataset at the path specified in the notebook.

The workflow writes model performance and prediction outputs to `Groundwater_Results.xlsx` and displays diagnostic plots.

## Reproducibility notes

The scripts set random seeds for selected libraries. Exact numerical results can still vary with package versions, hardware, and execution environment. Reproduction of the manuscript's results requires the same input data, preprocessing decisions, software environment, and model settings.

## Citation

If you use this code, please cite the associated research article when its bibliographic details become available.

## License

See the `LICENSE` file for the terms governing reuse of the code.

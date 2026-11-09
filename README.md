# Password Strength Checker — Fuzzy Logic Project

[![Python tests](https://github.com/kanizfatemar0xy/-Fuzzy-Logic-and-Neural-Networks/actions/workflows/python-tests.yml/badge.svg)](https://github.com/kanizfatemar0xy/-Fuzzy-Logic-and-Neural-Networks/actions/workflows/python-tests.yml)

An educational exploration of password-length and character-category features with fuzzy membership functions, developed by **Kaniz Fatema Roxy**.

## Two ways to explore
1. **`Password Strength Checker.ipynb`** — the original university scikit-fuzzy/Jupyter notebook, kept as an archival demonstration. It contains an interactive password prompt. **Use dummy strings, never real passwords.**
2. **`password_meter.py`** — a small standalone, testable, Python standard-library implementation that demonstrates fuzzy weak/medium/strong memberships. Its scoring formula is deliberately simplified and **is not numerically identical to the original notebook**.

## Run safely
```bash
python password_meter.py
python -m unittest discover -s tests -v
```
The terminal uses `getpass` to avoid echoing example input. Tests only use synthetic strings. No credentials are logged, stored, or transmitted.

### Run the archival notebook
Use Python 3, Jupyter, NumPy, Matplotlib and scikit-fuzzy; install requirements with `pip install -r requirements.txt`. Some notebook cells may have old output/Colab-specific commands; execution has not been certified as fully reproducible in every environment.

## Limitations
A high result **does not prove** that a password is safe. This example does not check data breaches, dictionaries, personal context, adversarial patterns or real-world attack costs. Use a reputable, breach-aware estimator for real decisions and enable MFA.

**Author:** [Kaniz Fatema Roxy](https://github.com/kanizfatemar0xy)

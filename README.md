# Fuzzy Password Strength Checker — Python & Fuzzy Logic

[![Python unit tests](https://github.com/kanizfatemar0xy/-Fuzzy-Logic-and-Neural-Networks/actions/workflows/python-tests.yml/badge.svg)](https://github.com/kanizfatemar0xy/-Fuzzy-Logic-and-Neural-Networks/actions/workflows/python-tests.yml)

**Python · Jupyter Notebook · scikit-fuzzy · Unit Testing**

An educational programming project by **Kaniz Fatema Roxy** exploring how password features can be represented using fuzzy membership concepts. It contains the original university notebook and a separate, lightweight Python implementation with automated tests.

**[View the Python implementation](password_meter.py)** · **[Open the notebook](Password%20Strength%20Checker.ipynb)** · **[See tests](tests/test_password_meter.py)** · **[Developer portfolio](https://kanizfatemar0xy.github.io/travel-website-project/portfolio.html)**

## What the project demonstrates

| Area | Example |
| --- | --- |
| Python fundamentals | Input validation, character categorisation, functions and dataclasses |
| Feature engineering | Length, character groups and unique-character ratio |
| Fuzzy concepts | Weak, medium and strong membership values |
| Testing | Synthetic test strings and repeatable unit tests |
| Safe interaction | Terminal input hidden using `getpass` |

## Getting started

**Option 1 — Python CLI (no third-party dependencies):**

```bash
python password_meter.py
```

The program asks for a **dummy test string** and prints an illustrative score and category. Never enter a password you actually use.

**Option 2 — Original Jupyter notebook:**

```bash
python -m pip install -r requirements.txt
jupyter notebook
```

Open `Password Strength Checker.ipynb` in Jupyter. It is an archived teaching notebook with scikit-fuzzy membership functions, plots and notebook-specific commands.

## Run automated checks

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs these unit tests on the Python demonstration module. The original notebook has **not** been fully validated by the same automated suite.

## Project structure

- [`password_meter.py`](password_meter.py) — simplified, testable Python CLI
- [`Password Strength Checker.ipynb`](Password%20Strength%20Checker.ipynb) — original university notebook
- [`tests/`](tests) — automated tests
- [`requirements.txt`](requirements.txt) — notebook dependencies
- [`.github/workflows/python-tests.yml`](.github/workflows/python-tests.yml) — continuous integration

## Limitations and security

This is **not a real-world password-security assessment tool**. Its score is a teaching heuristic, not an estimate of guessing cost, breach exposure or resistance to targeted attacks. The CLI and notebook use **different scoring methods** and should not be expected to produce identical numeric results. Use dummy data in both.

**Author:** [Kaniz Fatema Roxy](https://github.com/kanizfatemar0xy) · [Portfolio](https://kanizfatemar0xy.github.io/travel-website-project/portfolio.html) · [LinkedIn](https://www.linkedin.com/in/kaniz-fatema-roxy)

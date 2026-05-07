# ⚽ EPL 2025/26 Market Efficiency Dashboard

## Overview

This project is a football analytics dashboard built with Python and Streamlit that analyzes how Premier League teams perform relative to bookmaker expectations during the 2025/26 season.

Using betting market probabilities from Bet365 odds, the dashboard identifies:

* Teams outperforming expectations
* Teams underperforming expectations
* Market inefficiencies in football outcomes

The project combines sports analytics, probability modeling, and interactive dashboard development into a professional portfolio project.

---

## Objectives

The main objective of this project is to evaluate whether teams consistently exceed or fall short of market expectations.

The dashboard answers questions such as:

* Which teams are outperforming bookmaker predictions?
* Which teams are consistently underperforming?
* Are betting markets accurately pricing team strength?

---

## Dataset

Dataset: English Premier League (2025/26)

Key features include:

* Match outcomes
* Goals scored
* Betting odds
* Home and away statistics
* Referee information
* Market probabilities

---

## Tech Stack

* Python
* Pandas
* Streamlit
* Plotly
* OpenPyXL

---

## Methodology

### 1. Convert Odds to Probabilities

Bet365 odds are converted into implied probabilities:

* Home Win Probability
* Draw Probability
* Away Win Probability

### 2. Normalize Probabilities

Probabilities are normalized to remove bookmaker margin (overround).

### 3. Encode Match Outcomes

Match outcomes are encoded as:

* H → Home Win
* D → Draw
* A → Away Win

### 4. Calculate Overperformance

The model compares:
Actual Outcome − Expected Probability

Positive values:
→ Team exceeded expectations

Negative values:
→ Team underperformed expectations

---

## Dashboard Features

### 📊 Market Efficiency Rankings

Visualizes overperforming and underperforming teams.

### 🔍 Team Explorer

Interactive filtering for individual team performance.

### 📈 Interactive Visualizations

Dynamic Plotly charts integrated into Streamlit.

### ⚽ Betting Market Insights

Analyzes bookmaker expectations versus actual outcomes.

---

## Sample Insights

* Sunderland emerged as one of the strongest overperforming teams relative to bookmaker expectations.
* Wolves and Tottenham significantly underperformed relative to market pricing.
* Certain mid-table clubs consistently generated positive market inefficiencies.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/epl-market-efficiency-dashboard.git
```

### Navigate into Project

```bash
cd epl-market-efficiency-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app15.py
```

---

## Project Structure

```bash
├── app15.py
├── E0.xlsx
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Team logo integration
* Expected points model
* Predictive match outcome modeling
* Betting value detection
* Player-level analytics
* Streamlit cloud deployment

---

## Author

Stephen Yaw Ayamah

Aspiring Football Data Analyst | Sports Analytics | Python & Streamlit Projects

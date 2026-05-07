# ⚽ EPL 2025/26 Market Efficiency Dashboard

## Overview

This project is a football analytics dashboard built with Python and Streamlit that analyzes how Premier League teams perform relative to bookmaker expectations during the 2025/26 season.

Using betting market probabilities from Bet365 odds, the dashboard identifies:

* Teams outperforming expectations
* Teams underperforming expectations
* Market inefficiencies in football outcomes

The project combines sports analytics, probability modeling, and interactive dashboard development into a professional portfolio project.

---
# live demo: https://idhwtq88ytqykqkqfhph97.streamlit.app/

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

## Business Recommendations

Based on the analysis, the project highlights several opportunities for improving betting market efficiency and pricing responsiveness.

### 1. Improve Market Responsiveness

Some teams consistently outperform bookmaker expectations, suggesting that market adjustments may react slowly to emerging tactical or performance trends.

Recommendation:

* Increase weighting of recent form indicators
* Adjust team strength ratings more dynamically
* Incorporate momentum-based modeling

Business impact:

* Reduced pricing inefficiencies
* More adaptive market probabilities

---

### 2. Incorporate Bettor Behavior Analysis

Large clubs often attract significant emotional betting activity regardless of actual form.

Recommendation:

* Separate statistical probabilities from public sentiment indicators
* Monitor betting volume distortions on high-profile teams

Business impact:

* Better liability management
* Improved market balancing

---

### 3. Develop Market Inefficiency Monitoring Systems

This project demonstrates how dashboards can track teams consistently exceeding or underperforming implied probabilities.

Recommendation:

* Build internal monitoring systems for prediction error tracking
* Identify persistent market inefficiencies earlier

Business impact:

* Faster market recalibration
* Improved forecasting accuracy

---

### 4. Enhance Live Market Adjustments

Repeated overperformance patterns may indicate that odds adjustments are not reacting quickly enough to changing team dynamics.

Recommendation:

* Integrate rolling performance metrics
* Include injury, tactical, and momentum-based adjustments

Business impact:

* More accurate in-play pricing
* Better responsiveness to real-time developments

---

### 5. Combine Sports Analytics with Customer Behavior Insights

Betting markets are influenced not only by football performance but also by customer psychology and public sentiment.

Recommendation:

* Combine statistical modeling with bettor behavior analysis
* Segment recreational and professional betting patterns

Business impact:

* Stronger risk management
* More efficient pricing strategies

---

## Strategic Insight

This project demonstrates how data analytics can identify gaps between bookmaker expectations and actual football outcomes, supporting more informed decision-making in sports betting markets.


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

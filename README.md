## EPL 2025/26 Market Efficiency Dashboard
## Overview

This project is a quantitative football analytics dashboard built with Python and Streamlit that evaluates how Premier League teams perform relative to bookmaker-implied expectations during the 2025/26 season.

Using betting market probabilities derived from Bet365 odds, the system performs:

Market efficiency analysis
Team-level statistical significance testing
Rolling calibration monitoring
Structural deviation detection

The project combines sports analytics, probability modeling, and inferential statistics into a professional-grade quantitative dashboard.

## Live Demo

https://idhwtq88ytqykqkqfhph97.streamlit.app/

## Objectives

The primary objective is to determine whether observed outcomes significantly deviate from bookmaker expectations.

The dashboard answers:

Which teams outperform market probabilities?
Are deviations statistically significant?
Is home advantage properly calibrated?
Does market calibration remain stable over time?
Are there signs of structural drift?
Dataset

## English Premier League (2025/26)

Key features include:

Match results (FTR)
Goals scored (FTHG, FTAG)
Betting odds (B365H, B365D, B365A)
Home and away statistics
Market-implied probabilities
Time-series match data
## Tech Stack
Python
Pandas
Streamlit
Plotly
Statsmodels
OpenPyXL
## Methodology
1️⃣ Convert Odds to Probabilities

Decimal odds are transformed into implied probabilities:

Home Win Probability
Draw Probability
Away Win Probability
2️⃣ Normalize Probabilities

Bookmaker overround is removed by normalizing probabilities so that:

P
home
	​

+P
draw
	​

+P
away
	​

=1
3️⃣ Encode Match Outcomes

Outcomes are encoded as:

H → Home Win
D → Draw
A → Away Win
4️⃣ Team-Level Overperformance

The model computes:

Overperformance=Actual Win Rate−Expected Probability

This forms the basis of team efficiency ranking.

5️⃣ Statistical Significance Testing

Team-level deviations are evaluated using:

One-sample proportion Z-tests

This determines whether differences between expected and actual win rates are statistically significant.

Outputs include:

Z-score
P-value
Expected probability
Actual win rate
Significance flag
6️⃣ Rolling Calibration Analysis

To assess time stability, a rolling window approach is implemented:

Rolling Gap=Actual Home Win Rate−Expected Probability

This allows detection of:

Short-term calibration drift
Structural shifts
Market responsiveness dynamics
## Dashboard Features
📊 Market Efficiency Rankings

Visual ranking of teams by over/underperformance.

🔬 Statistical Test Table

Team-level Z-scores and p-values for significance validation.

📉 Rolling Calibration Monitoring

Time-series visualization of market calibration stability.

🔍 Team Explorer

Interactive filtering for detailed match-level inspection.

📈 Dynamic Visualizations

Interactive Plotly charts embedded in Streamlit.

## Key Analytical Insights
Home advantage in the EPL appears largely well calibrated.
Most team deviations are not statistically significant.
Only isolated structural outliers were detected.
Rolling calibration reveals short-term fluctuations but no persistent systemic bias.
The market demonstrates strong aggregate efficiency.
## Business Applications

This framework supports:

Market calibration validation
Drift detection systems
Risk monitoring pipelines
Model performance auditing
Betting market efficiency analysis
Quantitative forecasting validation

The methodology aligns with standards used in sports analytics and probabilistic trading environments.

## Strategic Value

This project demonstrates applied use of:

Probability calibration
Hypothesis testing
Multiple comparison awareness
Time-series monitoring
Quantitative efficiency measurement

It represents a structured approach to evaluating market pricing behavior in professional sports betting environments.

## Installation
Clone Repository
git clone https://github.com/yourusername/epl-market-efficiency-dashboard.git
Navigate to Project
cd epl-market-efficiency-dashboard
Install Dependencies
pip install -r requirements.txt
Run Application
streamlit run app15.py
## Project Structure
├── app15.py
├── E0.xlsx
├── requirements.txt
└── README.md
## Future Enhancements
Structural break detection
Confidence intervals for rolling gaps
Multi-league comparison
Expected points modeling
Predictive outcome modeling
Live market integration
Cloud deployment optimization
Author

## Stephen Yaw Ayamah

Aspiring Football Data Analyst
Sports Analytics | Probability Modeling | Quantitative Systems
Python & Streamlit Projects

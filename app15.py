import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="EPL Market Efficiency Dashboard",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("⚽ EPL 2025/26 Market Efficiency Dashboard")

st.markdown("""
This dashboard analyzes how Premier League teams perform
relative to bookmaker expectations using statistical testing
and rolling calibration analysis.
""")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_excel("E0.xlsx", engine="openpyxl")
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

df = load_data()

if df is None:
    st.stop()

# ---------------------------------------------------
# DATA PREPARATION
# ---------------------------------------------------

# Implied probabilities
df["home_prob"] = 1 / df["B365H"]
df["draw_prob"] = 1 / df["B365D"]
df["away_prob"] = 1 / df["B365A"]

# Normalize (remove overround)
total_prob = df["home_prob"] + df["draw_prob"] + df["away_prob"]
df["home_prob"] /= total_prob
df["draw_prob"] /= total_prob
df["away_prob"] /= total_prob

# Actual outcomes
df["actual_home_win"] = (df["FTR"] == "H").astype(int)

# ---------------------------------------------------
# TEAM-LEVEL PERFORMANCE
# ---------------------------------------------------

df["home_overperf"] = df["actual_home_win"] - df["home_prob"]

home_perf = df.groupby("HomeTeam")["home_overperf"].mean()

team_overperf = home_perf.sort_values(ascending=False)

# ---------------------------------------------------
# TEAM SUMMARY (TOP SECTION)
# ---------------------------------------------------

st.header("📈 League Overview – Team Performance Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Matches", len(df))
col2.metric("Teams Analyzed", df["HomeTeam"].nunique())
col3.metric("Average Market Gap", round(team_overperf.mean(), 3))

# ---------------------------------------------------
# TEAM RANKING CHART
# ---------------------------------------------------

st.subheader("📊 Team Performance vs Market Expectations")

top_n = st.slider("Number of Teams to Display", 5, 20, 10)

team_df = (
    team_overperf
    .head(top_n)
    .reset_index()
)

team_df.columns = ["Team", "Score"]

colors = ["green" if x > 0 else "red" for x in team_df["Score"]]

fig = px.bar(
    team_df,
    x="Score",
    y="Team",
    orientation="h",
    text="Score",
    title="EPL Market Efficiency Rankings"
)

fig.update_traces(marker_color=colors, texttemplate="%{text:.3f}")
fig.add_vline(x=0, line_dash="dash")

fig.update_layout(height=600)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# ROLLING CALIBRATION ANALYSIS
# ---------------------------------------------------

st.header("📉 Rolling Calibration Analysis")

window_size = st.slider(
    "Rolling Window Size",
    min_value=10,
    max_value=50,
    value=30
)

# Sort by date
df = df.sort_values("Date")

# Rolling calculations
df["rolling_expected"] = df["home_prob"].rolling(window_size).mean()
df["rolling_actual"] = df["actual_home_win"].rolling(window_size).mean()
df["rolling_gap"] = df["rolling_actual"] - df["rolling_expected"]

rolling_df = df.dropna(subset=["rolling_gap"])

fig2 = px.line(
    rolling_df,
    x="Date",
    y="rolling_gap",
    title="Rolling Calibration Gap (Actual − Expected)"
)

fig2.add_hline(y=0, line_dash="dash")
fig2.update_layout(height=500)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# TEAM EXPLORER
# ---------------------------------------------------

st.subheader("🔍 Team Explorer")

selected_team = st.selectbox(
    "Select Team",
    sorted(team_overperf.index)
)

team_matches = df[df["HomeTeam"] == selected_team]

st.dataframe(team_matches, use_container_width=True)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------

with st.expander("📂 View Raw Dataset"):
    st.dataframe(df, use_container_width=True)

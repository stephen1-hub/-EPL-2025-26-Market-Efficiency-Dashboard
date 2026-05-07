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
This dashboard analyzes which teams are outperforming or underperforming
bookmaker expectations in the 2025/26 Premier League season.
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

# Stop app if data fails
if df is None:
    st.stop()

# ---------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------

# Convert bookmaker odds to implied probabilities
df["home_prob"] = 1 / df["B365H"]
df["draw_prob"] = 1 / df["B365D"]
df["away_prob"] = 1 / df["B365A"]

# Normalize probabilities
total_prob = (
    df["home_prob"] +
    df["draw_prob"] +
    df["away_prob"]
)

df["home_prob"] /= total_prob
df["draw_prob"] /= total_prob
df["away_prob"] /= total_prob

# Encode actual outcomes
df["actual_home_win"] = (df["FTR"] == "H").astype(int)
df["actual_away_win"] = (df["FTR"] == "A").astype(int)

# ---------------------------------------------------
# OVERPERFORMANCE MODEL
# ---------------------------------------------------

# Actual outcome - expected probability
df["home_overperf"] = (
    df["actual_home_win"] - df["home_prob"]
)

df["away_overperf"] = (
    df["actual_away_win"] - df["away_prob"]
)

# Team-level aggregation
home_perf = (
    df.groupby("HomeTeam")["home_overperf"]
    .mean()
)

away_perf = (
    df.groupby("AwayTeam")["away_overperf"]
    .mean()
)

team_overperf = (
    home_perf + away_perf
).sort_values(ascending=False)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("⚙️ Dashboard Controls")

view_option = st.sidebar.selectbox(
    "Select Dashboard View",
    [
        "Top Overperformers",
        "Worst Performers",
        "All Teams"
    ]
)

top_n = st.sidebar.slider(
    "Number of Teams",
    min_value=5,
    max_value=20,
    value=10
)

selected_team = st.sidebar.selectbox(
    "Explore Team",
    sorted(team_overperf.index)
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------
if view_option == "Top Overperformers":

    filtered_data = (
        team_overperf
        .sort_values(ascending=False)
        .head(top_n)
    )

elif view_option == "Worst Performers":

    filtered_data = (
        team_overperf
        .sort_values(ascending=True)
        .head(top_n)
    )

else:

    filtered_data = (
        team_overperf
        .sort_values(ascending=True)
    )

# ---------------------------------------------------
# PREPARE CHART DATA
# ---------------------------------------------------
team_df = filtered_data.reset_index()

team_df.columns = [
    "Team",
    "Score"
]

# Color mapping
colors = [
    "green" if score > 0 else "red"
    for score in team_df["Score"]
]

# ---------------------------------------------------
# MAIN VISUALIZATION
# ---------------------------------------------------
st.subheader("📊 Team Performance vs Market Expectations")

fig = px.bar(
    team_df,
    x="Score",
    y="Team",
    orientation="h",
    text="Score",
    title="Premier League Market Efficiency Rankings"
)

# Apply colors
fig.update_traces(
    marker_color=colors,
    texttemplate="%{text:.3f}"
)

# Add zero line
fig.add_vline(
    x=0,
    line_width=2,
    line_dash="dash",
    line_color="white"
)

# Improve layout
fig.update_layout(
    xaxis_title="Over / Under Performance",
    yaxis_title="Team",
    title_font_size=20,
    height=700
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# TEAM EXPLORER
# ---------------------------------------------------
st.subheader(f"🔍 Team Explorer: {selected_team}")

team_matches = df[
    (df["HomeTeam"] == selected_team) |
    (df["AwayTeam"] == selected_team)
]

st.dataframe(
    team_matches[
        [
            "Date",
            "HomeTeam",
            "AwayTeam",
            "FTHG",
            "FTAG",
            "FTR",
            "B365H",
            "B365D",
            "B365A"
        ]
    ],
    use_container_width=True
)

# ---------------------------------------------------
# TEAM SUMMARY METRICS
# ---------------------------------------------------
st.subheader("📈 Team Summary")

col1, col2, col3 = st.columns(3)

matches_played = len(team_matches)

wins = len(
    team_matches[
        (
            (team_matches["HomeTeam"] == selected_team) &
            (team_matches["FTR"] == "H")
        ) |
        (
            (team_matches["AwayTeam"] == selected_team) &
            (team_matches["FTR"] == "A")
        )
    ]
)

avg_perf = round(
    team_overperf[selected_team],
    3
)

col1.metric(
    "Matches Played",
    matches_played
)

col2.metric(
    "Wins",
    wins
)

col3.metric(
    "Overperformance Score",
    avg_perf
)

# ---------------------------------------------------
# INSIGHT BOX
# ---------------------------------------------------
st.subheader("🧠 Key Insight")

st.info(
    """
    This dashboard compares actual match outcomes against bookmaker expectations.

    • Positive scores indicate teams outperforming market expectations.
    • Negative scores indicate teams underperforming market expectations.
    • Bookmaker probabilities are derived from Bet365 odds.
    """
)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------
with st.expander("📂 View Raw Dataset"):
    st.dataframe(df, use_container_width=True)
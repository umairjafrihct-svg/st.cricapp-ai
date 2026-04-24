import streamlit as st
import pandas as pd
import plotly.express as px

# ──────────────────────────────
# CSV LOAD KARO
# ──────────────────────────────
df = pd.read_csv("newfile.csv")

# ──────────────────────────────
# UI
# ──────────────────────────────
st.title("🏏 Player Performance")

player = st.selectbox("Select Player", df["Player"].tolist())

# Selected player ka row nikalo
row = df[df["Player"] == player].iloc[0]

# ──────────────────────────────
# GRAPH KE LIYE DATA READY KARO
# ──────────────────────────────
stats_df = pd.DataFrame({
    "Stat": ["100s", "50s", "4s", "6s", "0s"],
    "Count": [
        int(row["100"]),
        int(row["50"]),
        int(row["4s"]),
        int(row["6s"]),
        int(row["0"])
    ]
})

# ──────────────────────────────
# BAR GRAPH
# ──────────────────────────────
st.subheader(f"{player} - Stats Count")

fig = px.bar(
    stats_df,
    x="Stat",
    y="Count",
    text="Count",
    color="Stat",
    color_discrete_map={
        "100s": "#FFD700",
        "50s": "#C0C0C0",
        "4s": "#2ECC71",
        "6s": "#E74C3C",
        "0s": "#7F8C8D"
    }
)

fig.update_traces(
    textposition="outside",
    textfont_size=18,
    textfont_color="white",
    marker_line_color="white",
    marker_line_width=2
)

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(size=14, color="white"),
    xaxis_title="",
    yaxis_title="Count",
    showlegend=False,
    yaxis=dict(range=[0, stats_df["Count"].max() + 50])
)

fig.update_xaxes(tickfont=dict(size=18, color="white"))
fig.update_yaxes(tickfont=dict(size=12, color="white"))

st.plotly_chart(fig, use_container_width=True)

# ──────────────────────────────
# METRIC CARDS
# ──────────────────────────────
st.subheader("📊 Quick Stats")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("100s", int(row["100"]))
c2.metric("50s", int(row["50"]))
c3.metric("4s", int(row["4s"]))
c4.metric("6s", int(row["6s"]))
c5.metric("0s", int(row["0"]))


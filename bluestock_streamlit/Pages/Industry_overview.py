import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import load_data

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Industry Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Industry Overview")

# ==========================
# Load Data
# ==========================
aum = load_data("SELECT * FROM fact_aum")

# Convert date column safely
aum["date"] = pd.to_datetime(aum["date"], errors="coerce")

st.sidebar.header("⚙️ Filters")
years = sorted(aum["date"].dt.year.unique())

selected_year = st.sidebar.selectbox(
    "📅 Select Year",
    years,
    index=len(years)-1
)
fund_house = st.sidebar.selectbox(
    "🏦 Fund House",
    ["All"] + sorted(aum["fund_house"].unique())
)
min_aum = st.sidebar.slider(
    "💰 Minimum AUM (Lakh Cr)",
    float(aum["aum_lakh_crore"].min()),
    float(aum["aum_lakh_crore"].max()),
    float(aum["aum_lakh_crore"].min())
)
filtered_data = aum.copy()

filtered_data = filtered_data[
    filtered_data["date"].dt.year == selected_year
]

if fund_house != "All":
    filtered_data = filtered_data[
        filtered_data["fund_house"] == fund_house
    ]

filtered_data = filtered_data[
    filtered_data["aum_lakh_crore"] >= min_aum
]
st.sidebar.markdown("---")

st.sidebar.info(
    """
📊 **Industry Dashboard**

Analyze:

• AUM Growth

• Fund Houses

• Industry Trends

• Year-wise Performance
"""
)

# Remove rows with invalid dates
aum = aum.dropna(subset=["date"])

# ==========================
# KPI Cards
# ==========================
latest_date = aum["date"].max()

latest_data = aum[aum["date"] == latest_date]

total_aum = latest_data["aum_lakh_crore"].sum()

total_amcs = aum["fund_house"].nunique()

total_records = len(aum)

latest_year = latest_date.year

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Latest AUM",
        f"₹{total_aum:.2f} Lakh Cr"
    )

with col2:
    st.metric(
        "🏦 Fund Houses",
        total_amcs
    )

with col3:
    st.metric(
        "📅 Latest Year",
        latest_year
    )

with col4:
    st.metric(
        "📂 Records",
        total_records
    )

st.divider()

# ==========================
# Year Filter
# ==========================
years = sorted(aum["date"].dt.year.unique())

selected_year = st.selectbox(
    "Select Year",
    years,
    index=len(years)-1
)

filtered = aum[aum["date"].dt.year == selected_year]

# ==========================
# AUM Trend Chart
# ==========================
st.subheader("📈 Assets Under Management (AUM) Trend")

fig = px.line(
    filtered,
    x="date",
    y="aum_lakh_crore",
    color="fund_house",
    markers=True,
    template="plotly_white"
)

fig.update_layout(
    height=550,
    title="AUM Growth by Fund House",
    xaxis_title="Date",
    yaxis_title="AUM (Lakh Crore)",
    hovermode="x unified",
    legend_title="Fund House"
)

st.plotly_chart(fig, use_container_width=True)

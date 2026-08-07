import streamlit as st
from utils.database import load_data
import plotly.express as px

st.set_page_config(
    page_title="Investor Analytics",
    page_icon="👥",
    layout="wide"
)
query = """
SELECT *
FROM fact_transactions
"""

investor_data = load_data(query)

st.title("👥 Investor Analytics")
st.sidebar.header("📋 Dashboard Filters")
# ==========================
# Sidebar Filters
# ==========================

state = st.sidebar.selectbox(
    "Select State",
    ["All"] + sorted(investor_data["state"].unique().tolist())
)

age = st.sidebar.selectbox(
    "Select Age Group",
    ["All"] + sorted(investor_data["age_group"].unique().tolist())
)

gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + sorted(investor_data["gender"].unique().tolist())
)

transaction = st.sidebar.selectbox(
    "Transaction Type",
    ["All"] + sorted(investor_data["transaction_type"].unique().tolist())
)

# ==========================
# Apply Filters
# ==========================

filtered_data = investor_data.copy()

if state != "All":
    filtered_data = filtered_data[
        filtered_data["state"] == state
    ]

if age != "All":
    filtered_data = filtered_data[
        filtered_data["age_group"] == age
    ]

if gender != "All":
    filtered_data = filtered_data[
        filtered_data["gender"] == gender
    ]

if transaction != "All":
    filtered_data = filtered_data[
        filtered_data["transaction_type"] == transaction
    ] 


# ==========================
# Dashboard Summary
# ==========================

st.header("📊 Dashboard Summary")

total_investors = filtered_data["investor_id"].nunique()

total_investment = filtered_data["amount_inr"].sum()

total_states = filtered_data["state"].nunique()

total_cities = filtered_data["city"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Investors", f"{total_investors:,}")

with col2:
    st.metric("💰 Total Investment", f"₹{total_investment:,.0f}")

with col3:
    st.metric("🏦 States", total_states)

with col4:
    st.metric("🏙 Cities", total_cities)

# ==========================
# Age Group Distribution
# ==========================

col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("👥 Age Group Distribution")
    
    age_data = (
    filtered_data
    .groupby("age_group")["amount_inr"]
    .sum()
    .reset_index()
    )

    age_data = age_data.sort_values("amount_inr", ascending=False)

    fig = px.bar(
        age_data,
        x="amount_inr",
        y="age_group",
        orientation="h",
        text_auto=".2s",
        title="Investment by Age Group",
        color_discrete_sequence=["#5A3E36"]
    )

    fig.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=45, b=10),
    xaxis_title="Total Investment (₹)",
    yaxis_title="Age Group"
    )

    fig.update_yaxes(categoryorder="total ascending")


    st.plotly_chart(fig, width="stretch")

with col2:
    st.subheader("🚻 Gender Distribution")

    gender_data = (
        filtered_data
        .groupby("gender")["investor_id"]
        .count()
        .reset_index()
    )

    fig2 = px.pie(
        gender_data,
        names="gender",
        values="investor_id",
        hole=0.55,
        color="gender",
        color_discrete_map={
            "Male": "#5A3E36",
            "Female": "#C89B3C"
        }
    )

    fig2.update_traces(textinfo="percent+label")

    st.plotly_chart(fig2, width="stretch")

st.divider()
st.header("📍 Geographic Distribution")

state_data = (
    filtered_data
    .groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    state_data,
    x="amount_inr",
    y="state",
    orientation="h",
    text_auto=True,
    color_discrete_sequence=["#5A3E36"]
)

fig.update_layout(
    height=500,
    title="Top 10 States by Investment",
    yaxis=dict(categoryorder="total ascending")
)

st.plotly_chart(fig, width="stretch")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏙️ City Tier Distribution")

    tier_data = (
        filtered_data
        .groupby("city_tier")["investor_id"]
        .count()
        .reset_index()
    )

    fig = px.pie(
        tier_data,
        names="city_tier",
        values="investor_id",
        hole=0.6,
        color="city_tier",
        color_discrete_map={
           "T30":"#5A3E36",
            "B30":"#C89B3C"
    }
    )

    fig.update_traces(textinfo="percent+label")

    fig.update_layout(height=420)

    st.plotly_chart(fig, width="stretch")

with col2:

    st.subheader("🏙️ Top 10 Cities")

    city_data = (
        filtered_data
        .groupby("city")["amount_inr"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        city_data,
        x="amount_inr",
        y="city",
        orientation="h",
        text_auto=True,
        color_discrete_sequence=["#C89B3C"]
    )

    fig.update_layout(
        height=420,
        title="Highest Investment Cities",
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(fig, width="stretch")

st.divider()
st.header("💳 Transaction Insights")

transaction_data = (
    filtered_data
    .groupby("transaction_type")["amount_inr"]
    .sum()
    .reset_index()
)

fig = px.bar(
    transaction_data,
    x="transaction_type",
    y="amount_inr",
    text_auto=True,
    color="transaction_type",
    color_discrete_sequence=["#EFDFD6", "#5A3E36", "#C89B3C"]
)

fig.update_layout(
    title="Investment by Transaction Type",
    height=450,
    xaxis_title="Transaction Type",
    yaxis_title="Investment (₹)"
)

st.plotly_chart(fig, width="stretch")

payment_data = (
    filtered_data
    .groupby("payment_mode")["amount_inr"]
    .sum()
    .reset_index()
    .sort_values("amount_inr", ascending=False)
)

fig = px.bar(
    payment_data,
    x="amount_inr",
    y="payment_mode",
    orientation="h",
    text_auto=True,
    color_discrete_sequence=["#5A3E36"]
)

fig.update_layout(
    title="Investment by Payment Mode",
    height=450,
    xaxis_title="Investment (₹)",
    yaxis_title="Payment Mode"
)

st.plotly_chart(fig, width="stretch")



import streamlit as st
import plotly.express as px
from utils.database import load_data

st.set_page_config(
    page_title="Portfolio Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Portfolio Analytics")

st.sidebar.header("⚙️ Filters")

query = """
SELECT *
FROM fact_portfolio
"""

portfolio_data = load_data(query)

total_stocks = portfolio_data["stock_symbol"].nunique()
total_market_value = portfolio_data["market_value_cr"].sum()
total_sectors = portfolio_data["sector"].nunique()
average_weight = portfolio_data["weight_pct"].mean()

sector = st.sidebar.selectbox(
    "Select Sector",
    ["All"] + sorted(portfolio_data["sector"].unique())
)
stock = st.sidebar.selectbox(
    "Select Stock",
    ["All"] + sorted(portfolio_data["stock_name"].unique())
)
date = st.sidebar.selectbox(
    "Portfolio Date",
    sorted(portfolio_data["portfolio_date"].unique())
)
weight = st.sidebar.slider(
    "Minimum Weight %",
    0.0,
    float(portfolio_data["weight_pct"].max()),
    0.0
)
filtered_data = portfolio_data.copy()

if sector != "All":
    filtered_data = filtered_data[
        filtered_data["sector"] == sector
    ]

if stock != "All":
    filtered_data = filtered_data[
        filtered_data["stock_name"] == stock
    ]

filtered_data = filtered_data[
    filtered_data["weight_pct"] >= weight
]

filtered_data = filtered_data[
    filtered_data["portfolio_date"] == date
]

st.header("📊 Portfolio Summary")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("📈 Stocks", total_stocks)

with col2:
    st.metric(
        "💰 Market Value",
        f"₹{total_market_value:,.0f} Cr"
    )

with col3:
    st.metric(
        "🏭 Sectors",
        total_sectors
    )

with col4:
    st.metric(
        "⚖ Average Weight",
        f"{average_weight:.2f}%"
    )

# ==========================
# Charts Row
# ==========================

col1, col2 = st.columns([1.4, 1])

with col1:
    st.subheader("🏆 Top 10 Holdings by Market Value")

    top_holdings = (
        portfolio_data
        .sort_values("market_value_cr", ascending=False)
        .head(10)
    )

    fig = px.bar(
    top_holdings,
    x="market_value_cr",
    y="stock_name",
    orientation="h",
    text="market_value_cr",
    color="stock_name",
    color_discrete_sequence=[
        "#0F766E",
        "#14B8A6",
        "#2DD4BF",
        "#5EEAD4",
        "#99F6E4",
        "#CCFBF1",
        "#7DD3C7",
        "#2A9D8F",
        "#55C7B8",
        "#A8E6DD"
    ]
)
    fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="inside"
)

    fig.update_layout(
        height=500,
        yaxis=dict(autorange="reversed"),
        xaxis_title="Market Value (Cr)",
        yaxis_title="Stock",
        coloraxis_showscale=False,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    
    st.plotly_chart(fig, width="stretch")

# ========================================
# RIGHT SIDE - SECTOR DONUT
# ========================================

with col2:

    st.subheader("🥧 Sector Allocation")

    sector_data = (
        portfolio_data
        .groupby("sector")["market_value_cr"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        sector_data,
        names="sector",
        values="market_value_cr",
        hole=0.60,
        color_discrete_sequence=[
            "#0F766E",
            "#14B8A6",
            "#2DD4BF",
            "#5EEAD4",
            "#99F6E4",
            "#0D9488",
            "#115E59",
            "#134E4A"
        ]
    )

    fig2.update_traces(textinfo="percent+label")

    fig2.update_layout(
        height=500
    )

    st.plotly_chart(fig2, width="stretch")

st.divider()
st.header("📈 Portfolio Diversification")

col3, col4 = st.columns([1.2, 1])
with col3:

    st.subheader("🏭 Top 10 Sectors by Weight")

    sector_weight = (
        portfolio_data
        .groupby("sector")["weight_pct"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig3 = px.bar(
        sector_weight,
        x="weight_pct",
        y="sector",
        orientation="h",
        text_auto=".2f",
        color="weight_pct",
        color_continuous_scale=[
             "#CCFBF1",
             "#99F6E4",
             "#5EEAD4",
             "#14B8A6",
             "#0F766E"
]
           
        
    )

    fig3.update_layout(
        height=450,
        coloraxis_showscale=False,
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Weight (%)",
        yaxis_title=""
    )

    st.plotly_chart(fig3, width="stretch")

with col4:

    st.subheader("📊 Portfolio Weight Distribution")

    fig4 = px.histogram(
        portfolio_data,
        x="weight_pct",
        nbins=20,
        color_discrete_sequence=["#0F766E"]
    )

    fig4.update_layout(
        height=450,
        xaxis_title="Weight (%)",
        yaxis_title="Number of Holdings",
        bargap=0.08
    )

    st.plotly_chart(fig4, width="stretch")

st.divider()
st.header("📋 Portfolio Holdings")

search_stock = st.text_input(
    "🔍 Search Stock",
    placeholder="Type stock name..."
)
table_data = portfolio_data.copy()

if search_stock:
    table_data = table_data[
        table_data["stock_name"]
        .str.contains(search_stock,
                      case=False,
                      na=False)
    ]
table_data = table_data[
    [
        "stock_name",
        "sector",
        "weight_pct",
        "market_value_cr",
        "current_price_inr"
    ]
]
table_data.columns = [
    "Stock",
    "Sector",
    "Weight %",
    "Market Value (Cr)",
    "Current Price (₹)"
]
st.dataframe(
    table_data,
    width="stretch", 
    hide_index=True
)
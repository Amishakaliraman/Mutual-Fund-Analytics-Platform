import streamlit as st
from utils.database import load_data
import plotly.express as px
import pandas as pd



st.set_page_config(
    page_title="Fund Performance",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<h1 style='color:#0A66C2;'>
📈 Fund Performance Dashboard
</h1>
""", unsafe_allow_html=True)


st.sidebar.header("🎯 Dashboard Filters")

query = """
SELECT
    n.date,
    n.nav,
    f.scheme_name,
    f.fund_house,
    f.category,
    f.fund_manager,
    f.risk_category,
    f.expense_ratio_pct,
    f.benchmark
FROM fact_nav n
JOIN dim_fund f
ON n.amfi_code = f.amfi_code
"""

data = load_data(query)

# ==========================
# Latest NAV of All Funds
# ==========================

latest_query = """
SELECT
    f.scheme_name,
    MAX(n.date) AS latest_date,
    n.nav
FROM fact_nav n
JOIN dim_fund f
ON n.amfi_code = f.amfi_code
GROUP BY f.scheme_name
ORDER BY n.nav DESC
"""

latest_nav = load_data(latest_query)

# ==========================
# KPI Cards
# ==========================


total_funds = data["scheme_name"].nunique()

average_nav = data["nav"].mean()

highest_nav = data["nav"].max()

total_categories = data["category"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Total Funds", total_funds)

with col2:
    st.metric("📈 Average NAV", f"{average_nav:.2f}")

with col3:
    st.metric("🚀 Highest NAV", f"{highest_nav:.2f}")

with col4:
    st.metric("📂 Categories", total_categories)

# ==========================
# Fund Filter
# ==========================


fund_list = sorted(data["scheme_name"].unique())

selected_fund = st.sidebar.selectbox(
    "📈 Select a Fund",
    fund_list
)

filtered_data = data[data["scheme_name"] == selected_fund]

# ==========================
# Fund Information
# ==========================


fund_info = filtered_data.iloc[0]

st.subheader("📋 Fund Details")

col1, col2 = st.columns(2)

with col1:
    st.write("**Fund House:**", fund_info["fund_house"])
    st.write("**Category:**", fund_info["category"])
    st.write("**Fund Manager:**", fund_info["fund_manager"])

with col2:
    st.write("**Risk Category:**", fund_info["risk_category"])
    st.write("**Expense Ratio:**", f'{fund_info["expense_ratio_pct"]}%')
    st.write("**Benchmark:**", fund_info["benchmark"])

# ==========================
# Compare Multiple Funds
# ==========================

comparison_funds = st.sidebar.multiselect(
    "Compare Funds",
    options=fund_list,
    default=[selected_fund]
)

# ==========================
# NAV Trend Chart
# ==========================
st.header("📈 Performance Analysis")

filtered_data = filtered_data.copy()

filtered_data["date"] = pd.to_datetime(filtered_data["date"])

filtered_data = filtered_data.sort_values("date")

# ==========================
# Date Range Filter
# ==========================

min_date = filtered_data["date"].min()
max_date = filtered_data["date"].max()

start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

filtered_data = filtered_data[
    (filtered_data["date"] >= pd.to_datetime(start_date)) &
    (filtered_data["date"] <= pd.to_datetime(end_date))
]


fig = px.line(
    filtered_data,
    x="date",
    y="nav",
    title=f"NAV Trend - {selected_fund}",
    markers=True
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="NAV",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🏆 Top 10 Funds by Latest NAV")

top10 = latest_nav.sort_values(
    by="nav",
    ascending=False
).head(10)

fig2 = px.bar(
    top10,
    x="nav",
    y="scheme_name",
    orientation="h",
    title="Top 10 Funds",
    text="nav"
)

fig2.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=500
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("📊 NAV Comparison")

comparison_data = data[
    data["scheme_name"].isin(comparison_funds)
].copy()

comparison_data["date"] = pd.to_datetime(comparison_data["date"])

fig3 = px.line(
    comparison_data,
    x="date",
    y="nav",
    color="scheme_name",
    markers=True,
    title="NAV Comparison"
)

fig3.update_layout(height=500)

st.plotly_chart(fig3, use_container_width=True)
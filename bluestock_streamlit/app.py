import streamlit as st
from pathlib import Path

# ==========================================================
# Page Configuration
# ==========================================================
st.set_page_config(
    page_title="Bluestock Mutual Fund Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# Load CSS
# ==========================================================
css = Path("Assets/style.css")
def load_css():
    with open("Assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

if css.exists():
    st.markdown(
        f"<style>{css.read_text()}</style>",
        unsafe_allow_html=True,
    )

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("<br>", unsafe_allow_html=True)

    logo = Path("Assets/logo.png")

    if logo.exists():

        c1, c2, c3 = st.columns([1,2,1])

        with c2:
            st.image(str(logo), use_container_width=True)

    st.markdown(
        """
        <div style="text-align:center;margin-top:10px;">
        <h2 style="color:white;margin-bottom:0;">
        Bluestock
        </h2>

        <p style="color:#C8D6E5;margin-top:0;">
        Mutual Fund Analytics
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.page_link(
        "app.py",
        label="🏠 Home"
    )

    st.page_link(
        "Pages/Industry_Overview.py",
        label="📊 Industry Overview"
    )

    st.page_link(
        "Pages/Fund_Performance.py",
        label="📈 Fund Performance"
    )

    st.page_link(
        "Pages/Investor_Analytics.py",
        label="👥 Investor Analytics"
    )

    st.page_link(
        "Pages/Portfolio_Analytics.py",
        label="💼 Portfolio Analytics"
    )

    st.markdown("---")

    st.info(
        """
Indian Mutual Fund Industry

**AUM:** ₹81 Lakh Cr

**Folios:** 26.1 Cr

**Schemes:** 1908
"""
    )

    st.markdown("---")

    st.caption("Version 1.0")

# ==========================================================
# Hero
# ==========================================================

st.markdown("""
<div class="hero">

<h1>📊 Mutual Fund Analytics Platform</h1>

<p>
Track Mutual Fund Performance, Investor Behaviour,
Portfolio Holdings and Risk Analytics using an
interactive dashboard.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# KPI Cards
# ==========================================================

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "💰 Total AUM",
        "₹81 Lakh Cr",
        "+12.4%"
    )

with k2:
    st.metric(
        "🏦 Top AMCs",
        "10",
        "Tracked"
    )

with k3:
    st.metric(
        "📂 Datasets",
        "10",
        "Integrated"
    )

with k4:
    st.metric(
        "📈 Dashboards",
        "4",
        "Interactive"
    )

st.write("")
st.write("")

# ==========================================================
# Welcome
# ==========================================================

st.write("")
st.markdown("## 🚀 Explore Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="feature-card">
        <h3>📊 Industry Overview</h3>
        <p>View AUM growth, SIP trends, AMC performance and industry statistics.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>👥 Investor Analytics</h3>
        <p>Analyse demographics, geography, investment behaviour and SIP patterns.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">
        <h3>📈 Fund Performance</h3>
        <p>Compare CAGR, Sharpe Ratio, Alpha, Beta, Sortino and Returns.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>💼 Portfolio Analytics</h3>
        <p>Explore sector allocation, holdings, VaR, CVaR and portfolio risk.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================================
# Modules
# ==========================================================

st.header("🚀 Dashboard Modules")

left,right = st.columns(2)

with left:

    st.markdown("""
<div class="card">

<h3>📊 Industry Overview</h3>

<p>📈 AUM Trend Analysis</p>

<p>💰 SIP Growth</p>

<p>🏦 Top Fund Houses</p>

<p>📂 Category Distribution</p>

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>📈 Fund Performance</h3>

<p>📊 CAGR</p>

<p>⭐ Sharpe Ratio</p>

<p>📉 Alpha</p>

<p>📈 Beta</p>

<p>🎯 Sortino Ratio</p>

</div>
""",unsafe_allow_html=True)

with right:

    st.markdown("""
<div class="card">

<h3>👥 Investor Analytics</h3>

<p>👨 Demographics</p>

<p>🌍 Geography</p>

<p>💳 SIP Analysis</p>

<p>📈 Transaction Behaviour</p>

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>💼 Portfolio Analytics</h3>

<p>🏭 Sector Allocation</p>

<p>⚠ Value at Risk</p>

<p>📉 Conditional VaR</p>

<p>📊 Rolling Sharpe Ratio</p>

</div>
""",unsafe_allow_html=True)

st.write("")

# ==========================================================
# Bottom Section
# ==========================================================

st.markdown("---")

c1,c2,c3 = st.columns(3)

with c1:

    st.info(
"""
### 📈 Analytics

Advanced Mutual Fund
performance metrics.
"""
    )

with c2:

    st.info(
"""
### 👥 Investors

Investor behaviour,
geography and SIP insights.
"""
    )

with c3:

    st.info(
"""
### ⚠ Risk

Risk management through
VaR, CVaR and Sharpe.
"""
    )

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div class="footer">

Built using  Streamlit • Plotly • SQLAlchemy • Python

</div>
""",
unsafe_allow_html=True
)
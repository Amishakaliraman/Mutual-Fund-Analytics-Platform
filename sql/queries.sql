-- Query 1: top 5 funds by AUM
select 
    fund_house,
    Max(aum_crore) as aum_crore
from fact_aum
group by fund_house
order by aum_crore desc
limit 5;

-- Query 2: Avg NAV per month
select 
    strftime('%Y-%m', date) as month,
    Round(avg(nav), 2) as avg_nav
from fact_nav
group by month
order by month;

-- Query 3: SIP YoY growth
select 
    month,
    sip_inflow_crore,
    yoy_growth_pct
from fact_sip
where yoy_growth_pct is not null
order by month;

--Query 4 : Avg yoy growth by year
SELECT
    substr(month,1,4) as year,
    Round(AVG(yoy_growth_pct),2) as avg_yoy_growth
from fact_sip
where yoy_growth_pct is NOT NULL
group by year
order by year;

--Query 5: Transactions by state
SELECT
    state,
    count(*) as total_transactions,
    sum(amount_inr) as total_amount_inr,
    Round(Avg(amount_inr),2) as avg_transaction_amount
from fact_transactions
group by state
order by total_amount_inr DESC;

--Query 6: funds with expense_ratio < 1%
SELECT
    scheme_name,
    fund_house,
    category,
    plan,
    expense_ratio_pct,
    aum_crore,
    morningstar_rating,
    risk_grade
from fact_performance
where expense_ratio_pct < 1
order by expense_ratio_pct ASC;

--Query 7: latest benchmark value
SELECT
    index_name,
    Max(date) as Latest_date,
    Max(close_value) as Latest_close_value
from fact_benchmark
group by index_name
order by Latest_close_value;

--Query 8: Top Categories by Net inflow
SELECT
    category,
    Round(sum(net_inflow_crore),2) as total_net_inflow
from fact_category
group by category
order by total_net_inflow DESC;

--Query 9: Industry-wise Folio Distribution
SELECT
    month,
    total_folios_crore,
    equity_folios_crore,
    debt_folios_crore,
    hybrid_folios_crore,
    others_folios_crore
from fact_industry
order by month DESC
limit 12;

--Query 10: Avg Folio Distribution
SELECT
    Round(Avg(equity_folios_crore),2) as avg_equity,
    Round(Avg(debt_folios_crore),2) as avg_debt,
    Round(Avg(hybrid_folios_crore),2) as avg_hybrid
from fact_industry;

--Query 11: Top Portfolio Holdings
SELECT
    stock_name,
    sector,
    Round(SUM(weight_pct),2) as total_weight,
    Round(SUM(market_value_cr),2) as market_value
from fact_portfolio
group by stock_name,sector
order by total_weight DESC
LIMIT 10;

--Query 12: Fund Managers with Most Schemes
SELECT
    fund_manager,
    count(*) as total_schemes
from dim_fund
GROUP by fund_manager
order by total_schemes DESC;

--Query 13: BEST Risk_Adjusted Funds
SELECT
      d.scheme_name,
      d.fund_house,
      d.fund_manager,
      p.return_3yr_pct,
      p.sharpe_ratio,
      d.expense_ratio_pct,
      p.aum_crore
from dim_fund d
join fact_performance p
on d.amfi_code = p.amfi_code
where d.expense_ratio_pct < 1
and p.return_3yr_pct > 15
ORDER by p.sharpe_ratio Desc;
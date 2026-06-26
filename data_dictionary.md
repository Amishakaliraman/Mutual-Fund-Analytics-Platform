# Mutual Fund Analytics - Data Dictionary
This document describes the tables , columns , data types, business definations and source datasets used in the mutual fund Analytics Project.

## Source Files
|       CSV File            |   SQLite Table     |
|---------------------------|--------------------|
| fund_master.csv           | dim_fund           |
| aum.csv                   | fact_aum           |
| benchmark.csv             | fact_benchmark     |
| category.csv              | fact_category      |
| industry.csv              | fact_industry      |
| nav_history.csv           | fact_nav           |
| performance.csv           | fact_performance   |
| portfolio.csv             | fact_portfolio     |
| sip.csv                   | fact_sip           |
| investor_transactions.csv | fact_transactions  |


## Table : dim_fund

**Purpose:**

Stores master information about each mutual fund scheme, including fund details, category, investment requirements, and fund manager information.

| Column                | Data Type | Business Definition                        |
|-----------------------|-----------|--------------------------------------      |
| amfi_code             | BIGINT    | Unique AMFI scheme code                    |
| fund_house            | TEXT      | Name of the Asset Management Company (AMC) |
| scheme_name           | TEXT      | Name of the mutual fund scheme             |
| category              | TEXT      | Primary fund category                      |
| sub_category          | TEXT      | Sub-category of the fund                   |
| plan                  | TEXT      | Investment plan (Regular/Direct)           |
| launch_date           | TEXT      | Date the scheme was launched               |
| benchmark             | TEXT      | Benchmark index used for comparison        |
| expense_ratio_pct     | FLOAT     | Annual expense ratio (%)                   |
| exit_load_pct         | FLOAT     | Exit load charged on redemption (%)        |
| min_sip_amount        | BIGINT    | Minimum SIP investment amount (₹)          |
| min_lumpsum_amount    | BIGINT    | Minimum lump sum investment amount (₹)     |
| fund_manager          | TEXT      | Name of the fund manager                   |
| risk_category         | TEXT      | Risk level of the scheme                   |
| sebi_category_code    | TEXT      | SEBI classification code                   |


## Table: fact_aum

Purpose:
This table stores the monthly AUM details of different mutual fund houses.

Source:
aum.csv

|     Column     | Data Type |        Description              |
|----------------|-----------|---------------------------------|
| date           | TEXT      | Date of the record              |
| fund_house     | TEXT      | Name of the mutual fund company |
| aum_lakh_crore | FLOAT     | AUM in lakh crore               |
| aum_crore      | BIGINT    | AUM in crore                    |
| num_schemes    | BIGINT    | Number of schemes offered       |

## Table : fact_benchmark

Purpose:
Stores benchmark index values used to compare the performance of mutual fund schemes.

| Column      | Data Type |    Business Definition                         |
|-------------|-----------|------------------------------------------------|
| date        | TEXT      | Date on which the benchmark value was recorded |
| index_name  | TEXT      | Name of the benchmark index                    |
| close_value | FLOAT     | Closing value of the benchmark index           |

## Table : fact_category

Purpose:
Stores monthly net inflow data for different mutual fund categories.

| Column            | Data Type | Business Definition                          |
|-------------------|-----------|----------------------------------------------|
| month             | TEXT      | Month for which the inflow data is recorded  |
| category          | TEXT      | Mutual fund category                         |
| net_inflow_crore  | FLOAT     | Net inflow amount for the category (₹ Crore) |

## Table : fact_industry

Purpose:
Stores monthly industry-level folio statistics across different mutual fund categories.

| Column               | Data Type | Business Definition                            |
|----------------------|-----------|------------------------------------------------|
| month                | TEXT      | Month for which the folio data is recorded     |
| total_folios_crore   | FLOAT     | Total number of mutual fund folios (in crores) |
| equity_folios_crore  | FLOAT     | Number of equity fund folios (in crores)       |
| debt_folios_crore    | FLOAT     | Number of debt fund folios (in crores)         |
| hybrid_folios_crore  | FLOAT     | Number of hybrid fund folios (in crores)       |
| others_folios_crore  | FLOAT     | Number of folios in other fund categories      |

## Table : fact_nav

Purpose:
Stores daily NAV values of mutual fund schemes.

|    Column   | Data Type |   Business Definition    |
|-------------|-----------|--------------------------|
| date        | TEXT      | NAV date                 |
| amfi_code   | BIGINT    | Unique AMFI Scheme Code  | 
| nav         | FLOAT     | Net Asset Value per unit |

## Table : fact_transactions

Purpose:
Contains investor transaction details.

|      Column        | Data Type |    Business Definition      |
|--------------------|-----------|-----------------------------|
| investor_id        | TEXT      | Unique investor identifier  |
| transaction_date   | TEXT      | Date of transaction         |
| amfi_code          | BIGINT    | Scheme AMFI Code            |
| transaction_type   | TEXT      | SIP, Lumpsum or Redemption  |
| amount_inr         | BIGINT    | Transaction amount in INR   |
| state              | TEXT      | Investor state              |
| city               | TEXT      | Investor city               |
| city_tier          | TEXT      | Tier classification of city |
| age_group          | TEXT      | Investor age group          |
| gender             | TEXT      | Investor gender             |
| annual_income_lakh | FLOAT     | Annual income in lakhs      |
| payment_mode       | TEXT      | UPI, Net Banking, Cheque etc|
| kyc_status         | TEXT      | KYC completion status       |

## Table : fact_performance

Purpose:
Stores performance metrics of mutual fund schemes.

|      Column       | Data Type |  Business Definition   |
|-------------------|-----------|------------------------|
| amfi_code         | BIGINT    | Unique Scheme Code     |
| scheme_name       | TEXT      | Scheme Name            |
| fund_house        | TEXT      | AMC Name               |
| category          | TEXT      | Fund Category          |
| plan              | TEXT      | Regular / Direct       |
| return_1yr_pct    | FLOAT     | One year return (%)    |
| return_3yr_pct    | FLOAT     | Three year CAGR        |
| return_5yr_pct    | FLOAT     | Five year CAGR         |
| benchmark_3yr_pct | FLOAT     | Benchmark return       |
| alpha             | FLOAT     | Alpha                  |
| beta              | FLOAT     | Beta                   |
| sharpe_ratio      | FLOAT     | Risk-adjusted return   |
| sortino_ratio     | FLOAT     | Downside risk ratio    |
| std_dev_ann_pct   | FLOAT     | Annualized volatility  |
| max_drawdown_pct  | FLOAT     | Maximum drawdown       |
| aum_crore         | BIGINT    | Assets under Management|
| expense_ratio_pct | FLOAT     | Expense ratio          |
| morningstar_rating| BIGINT    | Morningstar rating     |
| risk_grade        | TEXT      | Risk category          |

 ## Table : fact_portfolio

Purpose:
Stores portfolio holdings of mutual fund schemes, including stock allocation, market value, and portfolio composition.

| Column            | Data Type | Business Definition                             |
|-------------------|-----------|-------------------------------------------------|
| amfi_code         | BIGINT    | Unique AMFI scheme code                         |
| stock_symbol      | TEXT      | Stock ticker symbol                             |
| stock_name        | TEXT      | Name of the stock                               |
| sector            | TEXT      | Industry sector of the stock                    |
| weight_pct        | FLOAT     | Percentage weight of the stock in the portfolio |
| market_value_cr   | FLOAT     | Market value of the holding (₹ Crore)           |
| current_price_inr | FLOAT     | Current market price of the stock (₹)           |
| portfolio_date    | TEXT      | Date of the portfolio snapshot                 |  

## Table : fact_sip

Purpose:

Stores monthly SIP (Systematic Investment Plan) statistics, including inflows, active accounts, AUM, and year-over-year growth.

|           Column         | Data Type |      Business Definition                |       
|--------------------------|-----------|------------------------------------------
| month                    | TEXT      | Month- the SIP data is recorded          |
|sip_inflow_crore          | BIGINT    | Total SIP inflow during the month      |
|active_sip_accounts_crore | FLOAT     | Total active SIP accounts            |
|new_sip_accounts_lakh     | FLOAT     | New SIP accounts opened during the month  |
|sip_aum_lakh_crore        | FLOAT     | SIP Assets Under Management       |
|yoy_growth_pct            | FLOAT     | Year-over-year growth percentage of SIP investments |

## Notes

- All data types are based on the SQLite database schema.
- Dates are stored in `YYYY-MM-DD` format wherever applicable.
- Monetary values are represented in Indian Rupees (₹), Crores, or Lakhs as specified.
- Percentage values are stored as numeric percentages.
- The data dictionary was prepared using the cleaned datasets loaded into the SQLite database.
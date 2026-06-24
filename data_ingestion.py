import pandas as pd 
fund_master= pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum_by_fund = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
monthly_sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category_inflows = pd.read_csv("data/raw/05_category_inflows.csv")
industry_folio_count = pd.read_csv("data/raw/06_industry_folio_count.csv")
scheme_performance = pd.read_csv("data/raw/07_scheme_performance.csv")
investor_transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
portfolio_holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark_indices = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Data loaded successfully!")

# Store in dictionary
datasets = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum_by_fund": aum_by_fund,
    "monthly_sip": monthly_sip,
    "category_inflows": category_inflows,
    "industry_folio_count": industry_folio_count,
    "scheme_performance": scheme_performance,
    "investor_transactions": investor_transactions,
    "portfolio_holdings": portfolio_holdings,
    "benchmark_indices": benchmark_indices
}

# Print details
for name, df in datasets.items():
    print("\n" + "="*60)
    print(f"Dataset: {name}")

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

# exploring Fund_Master dataset
fund_master.head()
fund_master.info()
fund_master.describe()
fund_master.columns

fund_master['fund_house'].unique()
fund_master['fund_house'].value_counts()
fund_master['fund_house'].nunique()
fund_master['scheme_name'].value_counts()

fund_master["category"].unique()
fund_master["category"].nunique()
fund_master["category"].value_counts()

fund_master["sub_category"].unique()
fund_master["sub_category"].nunique()
fund_master["sub_category"].value_counts()

fund_master["risk_category"].unique()
fund_master["risk_category"].value_counts()
fund_master["risk_category"].nunique()

# Understand the AMFI code
fund_master["amfi_code"].nunique()
len(fund_master) 
# If both have same value, it means AMFI code is unique for each scheme. So, we can use it as a primary key for the fund_master dataset.   

# Check which datasets have the "amfi_code" column
for name, df in datasets.items():
    if "amfi_code" in df.columns:
        print(name)

# every code in fund_master exists in nav_history
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Missing Codes:", len(missing_codes))

# Check which datasets have the "amfi_code" column
datasets_with_amfi = {
    "nav_history": nav_history,
    "scheme_performance": scheme_performance,
    "investor_transactions": investor_transactions,
    "portfolio_holdings": portfolio_holdings
}
fund_codes = set(fund_master["amfi_code"])

for name, df in datasets_with_amfi.items():
    codes_in_df = set(df["amfi_code"])
    missing_in_df = fund_codes - codes_in_df
    print(f"Dataset: {name}, Missing Codes: {len(missing_in_df)}")
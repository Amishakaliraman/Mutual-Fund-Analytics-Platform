Create Table dim_fund (
    amfi_code INT PRIMARY KEY,
    fund_house text,
    scheme_name text,
    category text,
    sub_category text,
    fund_manager text
);

Create Table dim_date (
    date_id INT PRIMARY KEY,
    date DATE,
    day INT,
    month INT,
    year INT,
    quarter INT
);

create Table fact_nav(
    nav_id int PRIMARY KEY AUTO_INCREMENT,
    amfi_code INT not null,
    date_id INT not null,
    nav FLOAT,

    foreign key (amfi_code) REFERENCES dim_fund(amfi_code),
    foreign key (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    amfi_code INTEGER NOT NULL,
    report_date_id INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(report_date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    date_id INTEGER NOT NULL,
    amfi_code INTEGER,
    aum_crore REAL,
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);


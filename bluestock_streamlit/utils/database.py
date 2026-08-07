from pathlib import Path

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

ROOT_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = ROOT_DIR / "database" / "bluestock_mf.db"


@st.cache_resource
def get_engine():
    engine = create_engine(f"sqlite:///{DATABASE_PATH.resolve()}")
    return engine


@st.cache_data
def load_data(query):
    engine = get_engine()
    return pd.read_sql(query, engine)
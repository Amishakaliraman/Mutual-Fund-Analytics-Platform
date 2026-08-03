import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Update this path if your database is stored somewhere else
DATABASE_PATH = "../database/bluestock_mf.db"

@st.cache_resource
def get_engine():
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")
    return engine

@st.cache_data
def load_data(query):
    engine = get_engine()
    return pd.read_sql(query, engine)
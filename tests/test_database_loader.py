import os
import sys

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "bluestock_streamlit"))

from utils.database import load_data


def test_load_data_from_fact_aum():
    df = load_data("SELECT * FROM fact_aum LIMIT 5")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "date" in df.columns
    assert "aum_lakh_crore" in df.columns

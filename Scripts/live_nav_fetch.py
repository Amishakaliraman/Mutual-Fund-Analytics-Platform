import requests
import pandas as pd
from plotly import data

# Fetch API data
url = "https://api.mfapi.in/mf/125497"
try:
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        print("API request successful!")

        nav_df = pd.DataFrame(data["data"])
        print(nav_df.head())
        
        nav_df.to_csv("data/raw/hdfc_top100_live_nav.csv", index=False)
        print("CSV saved successfully!")
    
    else:
        print(f"API request failed with status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching API data: {e}")

# Creating dataset for 5 schemes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

all_nav_data = []

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            nav_df["scheme_name"] = scheme_name
            nav_df["scheme_code"] = scheme_code

            all_nav_data.append(nav_df)

            print(f"{scheme_name} fetched successfully")

        else:
            print(f"Failed for {scheme_name}: {response.status_code}")

    except Exception as e:
        print(f"Error for {scheme_name}: {e}")
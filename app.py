import streamlit as st
import pandas as pd
from pathlib import Path
import os

st.set_page_config(layout="wide")
st.title("🛺 Ola Ride Insights")

# Debug: Show current folder
st.sidebar.write("Current folder:", os.getcwd())

folder = r"C:\Users\Prajna C\OneDrive\Documents\Ola Ride project4"
st.sidebar.write("Looking in:", folder)

# Dashboard
img_path = Path(folder) / "dashboard.png"
if img_path.exists():
    st.image(str(img_path), use_container_width=True)
  
else:
    st.warning("dashboard.png missing")

st.markdown("---")

# Files
files = ["Q1_Successful.csv", "Q2_AvgDist_Vehicle.csv", "Q3_Cust_Cancels.csv", 
         "Q4_Top5_Customers.csv", "Q5_Driver_Cancels.csv", "Q6_PrimeSedan_Ratings.csv",
         "Q7_UPI_Rides.csv", "Q8_AvgCustRating_Vehicle.csv", "Q9_Total_BookingValue.csv",
         "Q10_Incomplete_Rides.csv"]

for fname in files:
    fpath = Path(folder) / fname
    if fpath.exists():
        st.subheader(f"✅ {fname}")
        df = pd.read_csv(fpath)
        st.dataframe(df, use_container_width=True)
    else:
        st.error(f"❌ {fname} missing")

# st.success("🎉 Project Complete!")



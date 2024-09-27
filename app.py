import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# URL of the CSV file
csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E6%BF%83%E5%BA%A6.csv"

# Load the data
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(csv_url)

# Create the pandas profiling report
profile = ProfileReport(data, title="Food Micro Data Risk Profiling Report", explorative=True)

# Streamlit app
st.title('Pandas Profiling Report for Food Micro Data Risk')
st.write('This application generates a profiling report for the dataset.')

# Display the profiling report in the Streamlit app
st_profile_report(profile)

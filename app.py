from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# URL of the CSV file
#csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E6%BF%83%E5%BA%A6.csv"
csv_url = "https://raw.githubusercontent.com/kento-koyama/food_micro_data_risk/main/%E9%A3%9F%E4%B8%AD%E6%AF%92%E7%B4%B0%E8%8F%8C%E6%B1%9A%E6%9F%93%E5%AE%9F%E6%85%8B_%E6%B1%9A%E6%9F%93%E7%8E%87.csv"

食中毒細菌汚染実態_汚染率.csv
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
# Import your data
def load_data(url):
    return pd.read_csv(url)
df = load_data(csv_url) 
pyg_app = StreamlitRenderer(df)
 
pyg_app.explorer()
 

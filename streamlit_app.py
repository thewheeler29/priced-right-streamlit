# streamlit_app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Priced Right Auto CRM Dashboard", page_icon="🚗", layout="wide")

st.title("Priced Right Auto CRM – Streamlit Dashboard")

# --- Load CSV from the repo ---
@st.cache_data
def load_data():
    return pd.read_csv("data/leads.csv")  # relative path inside your repo

df = load_data()

# --- Show data ---
st.subheader("Leads")
st.dataframe(df, use_container_width=True)

# --- Optional: Refresh button ---
if st.button("Refresh data"):
    st.cache_data.clear()
    st.experimental_rerun()


# --- Patterns you can use later ---
# 1) CSV in repo:
# df = pd.read_csv("data/leads.csv")
# 2) Google Sheets:
#   use gspread + service account (store JSON fields in Streamlit Secrets)
# 3) Supabase/Postgres:
#   use supabase client (URL + anon key in Streamlit Secrets)
# 4) External API:
#   import requests; data = requests.get("https://...").json()

# streamlit_app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Priced Right Auto CRM Dashboard", page_icon="🚗", layout="wide")

st.title("Priced Right Auto CRM – Streamlit Dashboard")
st.caption("Starter app. Replace the sample data with your live source when ready.")

# Sample data (replace later)
df = pd.DataFrame([
    {"Lead": "John Doe", "Source": "Facebook", "Status": "New"},
    {"Lead": "Jane Smith", "Source": "Website", "Status": "Contacted"},
])

# Simple UI
left, right = st.columns([2, 1])
with left:
    st.subheader("Leads")
    st.dataframe(df, use_container_width=True)
with right:
    st.metric("Total Leads", len(df))

# --- Patterns you can use later ---
# 1) CSV in repo:
# df = pd.read_csv("data/leads.csv")
# 2) Google Sheets:
#   use gspread + service account (store JSON fields in Streamlit Secrets)
# 3) Supabase/Postgres:
#   use supabase client (URL + anon key in Streamlit Secrets)
# 4) External API:
#   import requests; data = requests.get("https://...").json()

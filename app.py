import streamlit as st
import requests
import pandas as pd
import time

API = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")
st.title("📦 Real-Time Warehouse Dashboard")

# ---------- AUTO REFRESH ----------
REFRESH_INTERVAL = 2  # seconds

# ---------- CONTROLS ----------
col_btn1, col_btn2 = st.columns([1, 1])

with col_btn1:
    if st.button("▶️ Generate Order"):
        try:
            requests.get(f"{API}/generate", timeout=2)
        except:
            st.error("Backend not reachable")

with col_btn2:
    if st.button("🔄 Reset System"):
        try:
            requests.get(f"{API}/reset", timeout=2)
        except:
            st.error("Backend not reachable")


# ---------- FETCH DATA ----------
def fetch_data():
    try:
        requests.get(f"{API}/generate", timeout=2)
        res = requests.get(f"{API}/dashboard", timeout=2)
        return res.json()
    except:
        return None


data = fetch_data()

if data is None:
    st.error("⚠️ Backend not running. Start FastAPI server.")
    st.stop()

# ---------- DATAFRAMES ----------
orders = pd.DataFrame(
    data["orders"],
    columns=["ID", "Product", "Quantity", "Status", "Time"]
)

inventory = pd.DataFrame(
    data["inventory"],
    columns=["Product", "Stock"]
)

# ---------- DASHBOARD ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Inventory Levels")
    st.bar_chart(inventory.set_index("Product"))

with col2:
    st.subheader("📈 Orders Distribution")
    st.bar_chart(orders["Product"].value_counts())

# ---------- LOW STOCK ALERT ----------
if data.get("low_stock"):
    st.error(f"⚠️ Low stock: {', '.join(data['low_stock'])}")

# ---------- TABLE ----------
st.subheader("📦 Recent Orders")
st.dataframe(orders, width="stretch")

# ---------- KPIs ----------
st.subheader("📌 Key Metrics")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Orders", len(orders))
k2.metric("Low Stock Items", (inventory["Stock"] < 20).sum())
k3.metric("Packed Orders", (orders["Status"] == "Packed").sum())
k4.metric("Shipped Orders", (orders["Status"] == "Shipped").sum())

# ---------- STATUS BREAKDOWN ----------
st.subheader("📊 Order Status Breakdown")
st.bar_chart(orders["Status"].value_counts())

# ---------- AUTO REFRESH ----------
time.sleep(REFRESH_INTERVAL)
st.rerun()
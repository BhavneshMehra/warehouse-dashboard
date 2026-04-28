# 📦 Real-Time Warehouse Analytics Dashboard

## 🚀 Overview
This project simulates an e-commerce warehouse system where:
- Orders are generated dynamically
- Inventory is updated in real-time
- Dashboard reflects live changes every 5 seconds

## 🧠 Features
- Real-time data simulation
- Inventory tracking
- Order processing visualization
- KPI metrics (orders, stock alerts, packed orders)

## 🛠 Tech Stack
- FastAPI (Backend)
- SQLite (Database)
- Streamlit (Frontend Dashboard)

## ▶️ Run Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start backend
uvicorn backend:app --reload

### 3. Start frontend
streamlit run app.py

## 🎯 Use Case
Designed as a demonstration for:
- Supply chain analytics
- Process automation
- Real-time dashboards
# 📦 Real-Time Warehouse Analytics & Automation Dashboard

## 🚀 Overview
This project is a real-time simulation of an e-commerce warehouse system, designed to demonstrate how modern data pipelines, analytics, and automation work together in supply chain operations.

It mimics a live production environment where:
- Orders are continuously generated
- Inventory levels are dynamically updated
- Operational metrics are computed in real time
- A dashboard reflects live system state with periodic refresh

The goal is to showcase end-to-end data flow from backend systems to business-facing dashboards, similar to real-world logistics and e-commerce platforms.

---

## 🎯 Key Highlights

- ⚡ Real-Time Simulation  
  Continuous order generation with automatic inventory updates

- 📊 Live Analytics Dashboard  
  Visual insights into inventory levels, order distribution, and system KPIs

- 📦 Order Lifecycle Modeling  
  Orders transition through realistic states: Pending → Packed → Shipped

- 🚨 Low Stock Detection  
  Automatic identification of products below threshold levels

- 🔄 Auto-Refreshing UI  
  Dashboard updates every 5 seconds to reflect latest system state

- 🧠 Business-Oriented Metrics  
  - Total orders processed  
  - Packed & shipped orders  
  - Low stock items  
  - Product demand distribution  

---

## 🧠 System Architecture

Random Data Generator  
        ↓  
SQLite Database  
        ↓  
FastAPI Backend (REST APIs)  
        ↓  
Streamlit Dashboard (Polling every 5s)

This architecture demonstrates:
- Backend-driven data pipelines  
- API-based communication  
- Real-time visualization layer  

---

## 🛠 Tech Stack

| Layer        | Technology  | Purpose                          |
|-------------|------------|----------------------------------|
| Backend      | FastAPI     | High-performance API layer        |
| Database     | SQLite      | Lightweight persistent storage    |
| Frontend     | Streamlit   | Interactive analytics dashboard   |
| Data Handling| Pandas      | Data transformation & analysis    |

---

## 📊 Dashboard Features

### 📈 Inventory Monitoring
- Real-time stock levels per product  
- Visual bar charts for quick insights  

### 📦 Order Analytics
- Distribution of orders across products  
- Recent orders table with timestamps  

### 📌 KPI Metrics
- Total orders processed  
- Packed vs shipped orders  
- Low stock alerts  

### 🚨 Alerts
- Highlights products with critically low inventory  

---

## ▶️ Run Instructions

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start backend server
uvicorn backend:app --reload

### 3. Launch dashboard
streamlit run app.py

### 4. Open in browser
- Dashboard: http://localhost:8501  
- API Docs: http://127.0.0.1:8000/docs  

---

## 🧪 Demo Flow

1. Start backend and dashboard  
2. Observe automatic order generation  
3. Watch inventory decrease dynamically  
4. Track order status transitions  
5. Monitor KPIs updating in real time  

---

## 🎯 Real-World Relevance

This project reflects real industry use cases such as:
- Warehouse operations monitoring  
- E-commerce fulfillment tracking  
- Business intelligence dashboards  
- Process automation systems  

---

## 🚀 Possible Extensions

- Demand forecasting using ML models  
- Delivery delay prediction  
- WebSocket-based real-time streaming  
- Multi-warehouse simulation  
- Integration with Power BI / Grafana  

---

## 🧠 Key Learnings

- Designing real-time data pipelines  
- Building API-driven systems  
- Translating raw data into business insights  
- Implementing fault-tolerant frontend-backend communication  

---

## 👨‍💻 Author

Bhavnesh Mehra

---

## ⭐ Why This Project Stands Out

This is not just a dashboard — it demonstrates:
- System design thinking  
- Real-time data engineering concepts  
- Business-oriented analytics  
- Practical implementation of supply chain workflows  

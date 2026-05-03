# 🚖 OLA Ride Insights – End-to-End Data Analytics Project

## Project Overview
This project focuses on analyzing ride-booking data from a ride-sharing platform (OLA) to uncover key business insights related to ride success, cancellations, revenue, and customer behavior.

The goal is to transform raw operational data into actionable insights that can help improve service efficiency, optimize driver allocation, and enhance customer experience.

This is a complete end-to-end analytics project covering data cleaning, querying, visualization, and deployment.

---

##  Problem Statement
Ride-sharing platforms generate massive volumes of data, but without proper analysis, it becomes difficult to identify operational inefficiencies and business opportunities.

Key challenges addressed in this project:
- High ride cancellation rates
- Driver availability and allocation issues
- Revenue tracking and optimization
- Customer and driver performance analysis
- Payment behavior trends

This project aims to solve these challenges using data-driven insights.

---

##  Tech Stack
- **Python** (Pandas, NumPy) → Data Cleaning & Preprocessing  
- **SQL (SQLite)** → Data Analysis & Querying  
- **Power BI** → Dashboard & Visualization  
- **Streamlit** → Web App Deployment  

---

##  Dataset Details
- ~103,000 ride records (July 2024)
- 20+ features including:
  - Booking status
  - Vehicle type
  - Ride distance
  - Payment method
  - Customer & driver ratings
  - Timestamps

---

##  Project Workflow

### 1. Data Cleaning & Preprocessing (Python)
- Handled missing values using business logic
- Removed duplicate records
- Standardized data formats
- Combined date & time into a single column
- Created new features:
  - `Is_Success`
  - `Revenue`
  - `Total_Rating`

---

### 2. SQL Analysis
Performed analytical queries to extract business insights:
- Success vs cancellation analysis
- Revenue calculation
- Customer behavior insights
- Driver performance evaluation
- Payment method trends

---

### 3. Power BI Dashboard
Developed an interactive dashboard with:
- KPI cards (Total Rides, Revenue, Success Rate)
- Ride trends over time
- Cancellation breakdown
- Revenue by payment method
- Ratings analysis
- Dynamic filters (Vehicle Type, Date, Booking Status)

---

### 4. Streamlit Web App
Built a lightweight web interface to:
- Display dashboard insights
- Show SQL query outputs
- Enable filtering, sorting, and downloading data
- Provide accessibility without Power BI dependency

---

##  Key Insights

- ✅ **62% Ride Success Rate** → Indicates operational inefficiency  
- ❌ **High Cancellation Rates**
  - 18% Driver-side cancellations
  - 10% Customer cancellations
  - 10% Driver not found  
- 💰 **₹35M Total Revenue** from successful rides  
- 📱 **40% Payments via UPI** → Strong digital adoption  
- ⭐ **Average Rating ~4.0** → Good but inconsistent service quality  

---

##  Business Recommendations

- Improve driver allocation to reduce cancellations  
- Optimize matching system to minimize "Driver Not Found" cases  
- Promote digital payments through incentives  
- Monitor driver performance for better service quality  

---

##  Project Outcome
- Built a complete analytics pipeline from raw data to insights  
- Delivered business-ready dashboard for decision-making  
- Created a user-friendly application for data access  

---

##  Project Deliverables
- Cleaned dataset (`ola_cleaned.csv`)
- SQL queries
- Power BI dashboard file
- Streamlit application
- Python notebook

---

##  Future Improvements
- Demand forecasting using time-series analysis  
- Cancellation prediction using machine learning  
- Real-time dashboard integration  
- Geographic analysis (heatmaps)  

---

##  Key Learnings
- Importance of data cleaning in analytics  
- Writing optimized SQL queries  
- Designing business-focused dashboards  
- Converting data insights into decisions  

---

##  Conclusion
This project demonstrates the ability to work on real-world business problems using data analytics. It highlights skills in data processing, querying, visualization, and delivering actionable insights for operational and strategic decision-making.

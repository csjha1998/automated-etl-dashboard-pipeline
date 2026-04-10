# 🚀 Automated ETL Dashboard Pipeline

## 📌 Overview
This project implements an end-to-end automated ETL (Extract, Transform, Load) pipeline that extracts data from PostgreSQL, processes it using Python, and updates a Google Sheets dashboard in real-time.

The pipeline is fully automated using Windows Task Scheduler, eliminating manual reporting and enabling continuous data updates.

---

## ⚙️ Architecture

- Data Source: PostgreSQL  
- Processing: Python (ETL pipeline using pandas)  
- Output: Google Sheets Dashboard  
- Automation: Task Scheduler (periodic execution)

---

## ✨ Features
- Automated data extraction from PostgreSQL  
- Data transformation using pandas  
- Google Sheets API integration (gspread)  
- Scheduled automation using Task Scheduler  
- Real-time dashboard updates  
- Logging and error handling  

---

## 🛠️ Tech Stack
- Python (pandas, gspread)  
- PostgreSQL  
- Google Sheets API  
- Task Scheduler  

---

## 📊 Dashboard
The dashboard provides:
- Total calls and conversions  
- Dealer-wise performance  
- Caller-wise performance report  
- Follow-up tracking  
- Online policies & COA tracking  
- Real-time KPI updates  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/csjha1998/automated-etl-dashboard-pipeline.git
cd automated-etl-dashboard-pipeline

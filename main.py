#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import psycopg2
import gspread
import logging
from google.oauth2.service_account import Credentials


# ---------------------------
# LOGGING SETUP
# ---------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# ---------------------------
# 1. DB CONNECTION
# ---------------------------
def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="test",
            user="postgres",
            password="Captainamerica@2025",
            port="5432"
        )
        logging.info("Connected to PostgreSQL")
        return conn
    except Exception as e:
        logging.error(f"DB Connection Failed: {e}")
        raise


# ---------------------------
# 2. EXTRACT DATA
# ---------------------------
def extract_data(conn):
    try:
        df_part = pd.read_sql("SELECT * FROM part_wise;", conn)
        df_cnc = pd.read_sql("SELECT * FROM cnc;", conn)
        df_grafana = pd.read_sql("SELECT * FROM grafana;", conn)

        logging.info("Data extracted successfully")
        return df_part, df_cnc, df_grafana

    except Exception as e:
        logging.error(f"Data extraction failed: {e}")
        raise


# ---------------------------
# 3. CLEAN DATA
# ---------------------------
def clean_df(df):
    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            df[col] = df[col].astype(str)

    df = df.fillna("")
    return df


# ---------------------------
# 4. CONNECT GOOGLE SHEETS
# ---------------------------
def connect_sheets():
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            r"C:\Users\CS Jha\OneDrive\Desktop\Projects\credentials.json",
            scopes=scope
        )

        client = gspread.authorize(creds)
        logging.info("Connected to Google Sheets")

        return client.open("NinjaCRM Dashboard")

    except Exception as e:
        logging.error(f"Google Sheets connection failed: {e}")
        raise


# ---------------------------
# 5. LOAD DATA
# ---------------------------
def upload_df(spreadsheet, df, sheet_name):
    try:
        sheet = spreadsheet.worksheet(sheet_name)
        sheet.clear()

        data = [df.columns.tolist()] + df.values.tolist()
        sheet.update(data)

        logging.info(f"{sheet_name} updated successfully")

    except Exception as e:
        logging.error(f"Upload failed for {sheet_name}: {e}")
        raise


# ---------------------------
# MAIN PIPELINE
# ---------------------------
def main():
    conn = None
    try:
        # Step 1: Connect DB
        conn = get_connection()

        # Step 2: Extract
        df_part, df_cnc, df_grafana = extract_data(conn)

        # Step 3: Clean
        df_part = clean_df(df_part)
        df_cnc = clean_df(df_cnc)
        df_grafana = clean_df(df_grafana)

        # Step 4: Connect Sheets
        spreadsheet = connect_sheets()

        # Step 5: Load
        upload_df(spreadsheet, df_part, "part_wise")
        upload_df(spreadsheet, df_cnc, "cnc")
        upload_df(spreadsheet, df_grafana, "grafana")

        logging.info("Pipeline executed successfully 🚀")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

    finally:
        if conn:
            conn.close()
            logging.info("DB connection closed")


if __name__ == "__main__":
    main()


# In[ ]:





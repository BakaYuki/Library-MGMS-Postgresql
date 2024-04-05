import psycopg2
import streamlit as st

# Database connection parameters
DB_NAME = "product_stock"
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"  # Update this if your database is hosted elsewhere
DB_PORT = "5432"  # Default PostgreSQL port

conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
)
cur = conn.cursor()
# Function to establish a connection to the PostgreSQL database
def create_connection():
    try:
        #conn = psycopg2.connect(**db_params)
        conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
)
        return conn
    except Exception as e:
        st.error(f"Error: Unable to connect to the database\n{e}")
        return None
    
    
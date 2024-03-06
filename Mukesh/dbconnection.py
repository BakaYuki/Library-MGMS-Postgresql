import streamlit as st
import psycopg2

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Database connection parameters
DB_NAME = "library_initial"
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
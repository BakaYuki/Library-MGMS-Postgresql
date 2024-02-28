import streamlit as st
import psycopg2

# Database connection parameters
DB_NAME = "library_management_system"
DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"  # Update this if your database is hosted elsewhere
DB_PORT = "5432"  # Default PostgreSQL port

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"


def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Login Successful!")
            return True
        else:
            st.error("Invalid username or password. Please try again.")
            return False
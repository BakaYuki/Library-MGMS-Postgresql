import streamlit as st
import psycopg2 

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
def add_book():
    st.subheader("Add New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    # publication_year = st.number_input("Publication Year", min_value=1000, max_value=3000)
    # isbn = st.text_input("ISBN")
    if st.button("Add"):
        # Insert the book information into the database
        try:
            cur.execute(
                "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)",
                (title, author, genre)
            )
            conn.commit()
            st.success("Book added successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding book: {e}")
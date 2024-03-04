
from dbconnection import *

def add_book():
    st.subheader("Add New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    # book_id = st.text_input("Book ID")
    if st.button("Add"):
        # Insert the book information into the database
        try:
            cur.execute(
                "INSERT INTO books (title, author, genre, book_id) VALUES (%s, %s, %s",
                (title, author, genre)
            )
            conn.commit()
            st.success("Book added successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding book: {e}")
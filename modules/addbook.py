
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
                "INSERT INTO books (title, author, genre) VALUES (%s, %s, %s)",
                (title, author, genre)
            )
            conn.commit()
            st.success("Book added successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding book: {e}")
            
# Function to retrieve all products from the database
def view_book():
    try :
        cur.execute("SELECT * FROM books ")
        book_list = cur.fetchall()
        # Display books in a table
        table_data = [("ID", "Book Name", "Author", "Genre")]
        for book in book_list:
            table_data.append((book[0], book[1], book[2], book[3]))
        st.table(table_data)

    except psycopg2.Error as e:
        st.error(f"Error searching for product: {e}")
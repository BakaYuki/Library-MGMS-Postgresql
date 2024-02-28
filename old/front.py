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

# Establish database connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

def issue_book():
    st.subheader("Issue Book")
    book_name = st.text_input("Enter the name of the book you want to search for:")
    if st.button("Search"):
        try:
            cur.execute(
                "SELECT book_id, title, author, stock FROM books WHERE title ILIKE %s AND stock > 0",
                ('%' + book_name + '%',)
            )
            books = cur.fetchall()
            if books:
                st.write("Matching Books:")
                for book in books:
                    book_id, title, author, stock = book
                    st.write(f"Title: {title}, Author: {author}, Stock: {stock}")
                    if st.button("Issue", key=f"issue_{book_id}"):
                        student_id = st.text_input("Enter your Student ID:")
                        try:
                            # Check if the student exists
                            cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
                            student = cur.fetchone()
                            if student:
                                # Issue the book
                                cur.execute(
                                    "INSERT INTO issued (student_id, book_id, issue_date) VALUES (%s, %s, CURRENT_DATE)",
                                    (student_id, book_id)
                                )
                                conn.commit()
                                cur.execute("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))
                                conn.commit()
                                st.success("Book issued successfully!")
                            else:
                                st.error("Invalid Student ID. Please enter a valid ID.")
                        except psycopg2.Error as e:
                            conn.rollback()
                            st.error(f"Error issuing book: {e}")
            else:
                st.write("No matching books found with available stock.")
        except psycopg2.Error as e:
            st.error(f"Error searching for books: {e}")
            

def return_book():
    st.subheader("Return Book")
    # Add code for returning a book here

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

def student_panel():
    student_option = st.sidebar.selectbox("Choose Option", ["Issue Book", "Return Book"])
    
    if student_option == "Issue Book":
        issue_book()
    elif student_option == "Return Book":
        return_book()
    
def admin_panel():
    st.title("Admin Panel")
    admin_option = st.sidebar.selectbox("Choose Option", ["Add Book", "Update Book", "Add Student", "Log Out"])
    
    if admin_option == "Add Book":
        add_book()
    elif admin_option == "Update Book":
        update_book()  # You need to implement this function
    elif admin_option == "Add Student":
        add_student()  # You need to implement this function
    elif admin_option == "Log Out":
        st.write("Log out functionality goes here")  # You need to implement this function
        return False
    
def main():
    st.title("Library Management System")
    
    # Options for User Selection
    option = st.sidebar.selectbox("Choose Option", ["Student", "Admin Login"])

    if option == "Student":
        student_panel()
    elif option == "Admin Login":
        logincheck = admin_login()
        while logincheck==True:
            logincheck  = admin_panel()
            


if __name__ == "__main__":

    main()


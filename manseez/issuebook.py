from dbconnection import *

def issue_book(): 
    
    st.subheader("Issue Book")
    book_name = st.text_input("Enter the name of the book you want to search for:")
    if st.button("Search"):
        try:
            cur.execute(
                "SELECT book_id, title, author FROM books WHERE title ILIKE %s",
                ('%' + book_name + '%',)
            )
            books = cur.fetchall()
            if books:
                st.write("Matching Books:")
                for book in books:
                    book_id, title, author = book
                    st.write(f"Title: {title}, Author: {author}")
               
                    if st.button("Issues", key=book_id):
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
                                # conn.commit()
                                # cur.execute("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))
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
            
            
            
            
            
            
            
            
            
# Trials            
            
def std_show(book_id):
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
            # conn.commit()
            # cur.execute("UPDATE books SET stock = stock - 1 WHERE book_id = %s", (book_id,))
            conn.commit()
            st.success("Book issued successfully!")
            
        else:
            st.error("Invalid Student ID. Please enter a valid ID.")
    except psycopg2.Error as e:
        conn.rollback()
        st.error(f"Error issuing book: {e}")

# from dbconnection import *
# import streamlit as st

# def issue_book():

#     st.subheader("Issue Book")
#     book_name = st.text_input("Enter the name of the book you want to search for:")
#     if st.button("Search"):
#         try:
#             cur.execute(
#                 "SELECT book_id, title, author FROM books WHERE title ILIKE %s",
#                 ('%' + book_name + '%',)
#             )
#             books = cur.fetchall()
#             if books:
#                 st.write("Matching Books:")
#                 for book in books:
#                     book_id, title, author = book
#                     st.write(f"Title: {title}, Author: {author}")
#                     if st.button(f"Issue {title} by {author}"):
#                         st.session_state.selected_book_id = book_id
#             else:
#                 st.write("No matching books found with available stock.")
#         except psycopg2.Error as e:
#             st.error(f"Error searching for books: {e}")

#     if "selected_book_id" in st.session_state:
#         student_id = st.text_input("Enter your Student ID:")
#         if st.button("Issue"):
#             try:
#                 # Check if the student exists
#                 cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
#                 student = cur.fetchone()
#                 if student:
#                     # Issue the book
#                     cur.execute(
#                         "INSERT INTO issued (student_id, book_id, issue_date) VALUES (%s, %s, CURRENT_DATE)",
#                         (student_id, st.session_state.selected_book_id)
#                     )
#                     conn.commit()
#                     st.success("Book issued successfully!")
#                 else:
#                     st.error("Invalid Student ID. Please enter a valid ID.")
#             except psycopg2.Error as e:
#                 conn.rollback()
#                 st.error(f"Error issuing book: {e}")



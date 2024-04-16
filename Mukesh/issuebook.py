from dbconnection import *

def issue_book(): 
    if 'issue_condition' not in st.session_state:
        st.session_state.issue_condition = False
    st.subheader("Issue Book")
    book_name = st.text_input("Enter the name of the book you want to search for:")
    if st.button("Search"):
        st.session_state.issue_condition = False
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
                    st.write(f"ID: {book_id}, Title: {title}, Author: {author}")

            else:
                st.write("No matching books found with available stock.")
        except psycopg2.Error as e:
            st.error(f"Error searching for books: {e}")
    issue_book_no = st.text_input("Enter the book id here to issue: ")
    st.session_state.book_no = issue_book_no
    if st.button("Issue"):
        st.session_state.issue_condition = True
    
    if st.session_state.issue_condition == True:
        try:
            cur.execute("SELECT * FROM books WHERE book_id = %s", (st.session_state.book_no,))
            book_id_check = cur.fetchone()
            if book_id_check:
                student_id = st.text_input("Enter your Student ID:") 
                if st.button("Confirm"):
                    try:
                        # Check if the student exists
                        cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
                        student = cur.fetchone()       
                        if student:
                            issue_date = date.today()
                            # Issue the book
                            cur.execute(
                                "INSERT INTO issued (student_id, book_id, issue_date) VALUES (%s, %s, %s)",
                                (student_id, st.session_state.book_no,issue_date,)
                            )
                            conn.commit()
                            st.success("Book issued successfully!")
                            st.session_state.issue_condition = False
                            
                        else:
                            st.error("Invalid Student ID. Please enter a valid ID.")
                    except psycopg2.Error as e:
                        conn.rollback()
                        st.error(f"Error issuing book: {e}")
            
            else:
                st.error("No such book found")
        except psycopg2.Error as e:            
            st.error(f"Error searching for books id: {e}")
        
            
            
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



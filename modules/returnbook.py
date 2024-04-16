from dbconnection import *

def return_book():
    st.subheader("Return Book")
    student_id = st.text_input("Enter your Student ID:")
    if st.button("Show Books Issued") and student_id!="":
        # Retrieve books issued to the student from the database
        try:
            cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
            check = cur.fetchone()
            if check:
                student_id, name, email = check
                st.write(f'Welcome {name}')
                try:
                    cur.execute(
                        "SELECT books.book_id, books.title, books.author, books.genre, issued.issue_date FROM issued JOIN books ON issued.book_id = books.book_id WHERE issued.student_id = %s",
                        (student_id,)
                    )
                    issued_books = cur.fetchall()
                    
                    if issued_books:
                        st.write("Books Issued to You:")
                        for book_id, title, author, genre, issue_date in issued_books:
                            st.write(f"ID: {book_id}, Title: {title}, Author: {author}, Genre: {genre}, Date Issued: {issue_date}")
                            # if st.button(f"Return {title}"):
                            #     # Implement book return logic here
                            #     st.success(f"Book '{title}' returned successfully!")
                    else:
                        st.write("No books currently issued to you.")
                except psycopg2.Error as e:
                    st.error(f"Error retrieving issued books: {e}")    
            else:
                st.error("No such student found")
        except psycopg2.Error as e:
            st.error(f"Error retrieving student: {e}")
    book_id = st.text_input("Enter the book id here to return: ")
    if st.button("Return") and book_id!="":
        try:
            cur.execute("SELECT * FROM issued WHERE book_id = %s AND student_id = %s", (book_id, student_id))
            issued_book = cur.fetchone()
            if issued_book:
                cur.execute("DELETE FROM issued WHERE book_id = %s AND student_id = %s", (book_id, student_id))
                conn.commit()
                st.success("Book returned successfully!")
            else:
                st.error("No such book found")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error returning book: {e}")
        

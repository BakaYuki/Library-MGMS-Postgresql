from dbconnection import *

def return_book():
    st.subheader("Return Book")
    student_id = st.text_input("Enter your Student ID:")
    if st.button("Show Books Issued"):
        # Retrieve books issued to the student from the database
        try:
            cur.execute(
                "SELECT books.book_id, books.title FROM issued_books JOIN books ON issued_books.book_id = books.book_id WHERE issued_books.student_id = %s",
                (student_id,)
            )
            issued_books = cur.fetchall()
            
            if issued_books:
                st.write("Books Issued to You:")
                for book_id, title in issued_books:
                    if st.button(f"Return {title}"):
                        # Implement book return logic here
                        st.success(f"Book '{title}' returned successfully!")
            else:
                st.write("No books currently issued to you.")
        except psycopg2.Error as e:
            st.error(f"Error retrieving issued books: {e}")


from dbconnection import *

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
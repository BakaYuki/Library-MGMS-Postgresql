from dbconnection import *

def update_book():
    st.subheader("Update Book")
    book_id = st.text_input("Book ID")

    
    if st.button("Update Book"):
        try:
            cur.execute("SELECT * FROM books WHERE book_id = %s", (book_id))
            book = cur.fetchone()
            if book:
                st.write("Matching Book:")
                book_id, name, author, genre, availability = book
                st.write(f"ID: {book_id}, Name: {name}, Author: {author}, Genre: {genre}, Availability: {availability}")
                # Show option to change name, author, genre, availability
            else:
                st.write("No matching book found.")
        
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error searching for books id: {e}")
            
            
    book_name = st.text_input("Book Name")
    book_author = st.text_input("Book Author")
    book_genre = st.text_input("Book Genre")
    book_availability = st.text_input("Book Availability True or False")    
        # try:
        #     cur.execute(
        #         "UPDATE books SET name = %s, author = %s WHERE book_id = %s",
        #         (book_name, book_author,book_id)
        #     )
        #     conn.commit()
        #     st.success("Book updated successfully!")
        # except psycopg2.Error as e:
        #     conn.rollback()
        #     st.error(f"Error updating book: {e}")
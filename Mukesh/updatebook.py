from dbconnection import *

def update_book():
    st.subheader("Update Book")
    book_id = st.text_input("Book ID")
    new_name = str()
    new_author = str()
    new_genre = str()
    new_availability = str()
    #Checking if the book exists
    if st.button("Search Book ID"):
        # status = 1
        # try:
        cur.execute("SELECT * FROM books WHERE book_id = %s", (book_id))
        book = cur.fetchone()
        if book:
            st.write("Matching Book:  ")
            book_id, name, author, genre, availability = book
            st.write(f"ID: {book_id}   \nName: {name}  \nnAuthor: {author}  \nGenre: {genre}  \nAvailability: {availability}")
            # Show option to change name, author, genre, availability
            new_name = st.text_input("New Name")
            new_author = st.text_input("New Author")
            new_genre = st.text_input("New Genre")
            new_availability = st.text_input("New Availability (True or False)")
            if st.button("Update"):
                st.write("Updating book")
                try:
                    cur.execute(
                        "UPDATE books SET name = %s, author = %s, genre = %s, availability = %s WHERE book_id = %s",
                        (new_name or name, new_author or author, new_genre or genre, new_availability or availability, book_id)
                    )
                    conn.commit()
                    st.success("Book updated successfully!")
                except psycopg2.Error as e:
                    conn.rollback()
                    st.error(f"Error updating book: {e}")
                else:
                    st.write("No matching book found.")
        
        # except psycopg2.Error as e:
        #     conn.rollback()
            # st.error(f"Error searching for books id: {e}")
    # while(status == 1):
    
            
 
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
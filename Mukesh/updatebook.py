from dbconnection import *

def update_book():
    st.subheader("Update Book")
    #Session State hold the book_id entered by the user even after page refresh
    st.session_state.book_id = st.text_input("Enter the Book ID:")
    book_id = st.session_state.book_id
    
    # Initialize Button Clicked state to False during starting
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False
    
    #Session State to True when button is clicked so that the book information can be displayed and updated
    if st.button("Show Book"):
        st.session_state.button_clicked = True
    
    # If the button is clicked, retrieve the book information from the database
    if st.session_state.button_clicked == True:  
        # Retrieve book information from the database
        book_id = int(book_id)
        cur.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
        book = cur.fetchone()
        
        #Display the book information in the form
        if book:
            # book_id, title, author, genre, availability = book
            book_id = book[0]
            title = book[1]
            author = book[2]
            genre = book[3]
            availability = book[4]
            #Book ID displayed only and cannot be changed
            st.write(f"Book ID: {book_id}")
            #value = shows the current information from the database
            title = st.text_input("Title", value=title) 
            author = st.text_input("Author", value=author)
            genre = st.text_input("Genre", value=genre)
            availability=  st.text_input("Availability", value=availability)
            if st.button("Update"):
                # Update the book information in the database
                try:
                    cur.execute(
                        "UPDATE books SET title = %s, author = %s, genre = %s WHERE book_id = %s",
                        (title, author, genre, book_id)
                    )
                    conn.commit()
                    st.success("Book updated successfully!")
                except psycopg2.Error as e:
                    conn.rollback()
                    st.error(f"Error updating book: {e}")
        else:
            st.error("No such book found")
            conn.rollback()
    else:
        conn.rollback()
    
    st.session_state.button_clicked = False
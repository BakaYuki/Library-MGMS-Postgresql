import streamlit as st

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Searching book
def issue_book():
    st.subheader("Issue Book")
    book_name = st.text_input("Enter the name of the book you want to search for:")
    if st.button("Search"):
        # Add code to search for the book
        st.write(f"Searching for book: {book_name}")

# Returning book
def return_book():
    st.subheader("Return Book")
    # Add code for returning a book here

#Admin Login
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

def main():
    st.title("Library Management System")
    option = st.sidebar.selectbox("Choose Option", ["Issue Book", "Return Book", "Admin Login"])

    if option == "Issue Book":
        issue_book()
    elif option == "Return Book":
        return_book()
    elif option == "Admin Login":
        if admin_login():
            # Show admin options once logged in
            st.sidebar.subheader("Admin Options")
            # Add admin options here

if __name__ == "__main__":
    main()

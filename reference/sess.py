import streamlit as st

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Login Successful!")
        else:
            st.error("Invalid username or password. Please try again.")

def admin_panel():
    st.title("Admin Panel")
    if st.session_state.get('admin_logged_in', False):
        # Add your admin panel functionality here
        admin_option = st.sidebar.selectbox("Choose Option", ["Add Book", "Update Book", "Add Student", "Log Out"])
        if admin_option == "Log Out":
            st.session_state.admin_logged_in = False
            st.write("Logged out successfully!")
    else:
        st.error("You need to log in as an admin first.")

def main():
    st.title("Library Management System")
    option = st.sidebar.selectbox("Choose Option", ["Student", "Admin Login"])

    if option == "Student":
        # Add your student panel functionality here
        pass
    elif option == "Admin Login":
        if 'admin_logged_in' not in st.session_state:
            st.session_state.admin_logged_in = False
        admin_login()

    admin_panel()

if __name__ == "__main__":
    main()

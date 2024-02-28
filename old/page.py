import streamlit as st
from add_book import *
# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"


# class SessionState:
#     def __init__(self,**kwargs):
#         self.__dict__.update(kwargs)


# #Initialize Session State
# session_state = SessionState(admin_logged_in=False)


def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Login Successful!")
            st.session_state.admin_logged_in = True
            return True
        else:
            st.error("Invalid username or password. Please try again.")
            return False


def admin_panel():
    # admin_login()
    if st.session_state.get('admin_logged_in', True):
        st.title("Admin Panel")
        admin_option = st.sidebar.selectbox("Choose Option", ["Add Book", "Update Book", "Add Student", "Log Out"])
        
        if admin_option == "Add Book":
            add_book()
            st.write("Add book functionality goes here")  # You need to implement this function
        elif admin_option == "Update Book":
            # update_book()  # You need to implement this function
            st.write("Update book functionality goes here")  # You need to implement this function
        elif admin_option == "Add Student":
            # add_student()  # You need to implement this function
            st.write("Add student functionality goes here")  # You need to implement this function
        elif admin_option == "Log Out":
            st.write("Log out functionality goes here")  # You need to implement this function
            st.session_state.admin_logged_in = False

def student_panel():
    student_option = st.sidebar.selectbox("Choose Option", ["Issue Book", "Return Book"])
    
    if student_option == "Issue Book":
        # issue_book()
        st.write("Issue book functionality goes here")
    elif student_option == "Return Book":
        # return_book()
        st.write("Return book functionality goes here")



def main():
    st.title("Library Management System")
    user_type = st.sidebar.selectbox("Select User Type", ["User", "Admin"])

    if user_type == "User":
        student_panel()
        # st.write("User Panel")
    elif user_type == "Admin":
        if 'admin_logged_in' not in st.session_state:
            st.session_state.admin_logged_in = False
        admin_login()
    admin_panel()
if __name__ == "__main__":
    main()

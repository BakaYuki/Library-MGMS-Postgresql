from dbconnection import *
from addbook import *
from addstudent import *
from updatebook import *

def admin_login():
    st.subheader("Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Login Successful!")
            st.empty()
            st.session_state.admin_logged_in = True
            admin_panel()
        else:
            st.error("Invalid username or password. Please try again.")


def admin_panel():
    
    if st.session_state.get('admin_logged_in', True):
        st.title("Admin Panel")
        admin_option = st.sidebar.selectbox("Choose Option", ["Add Book", "Update Book", "Add Student", "Log Out"])
        
        if admin_option == "Add Book": # Adding book functionality
            add_book()

        elif admin_option == "Update Book":
            update_book()
            
            # st.write("Update book functionality goes here")  
            
        elif admin_option == "Add Student":
            add_student()  # add student functionality

            # st.write("Add student functionality goes here")  

        elif admin_option == "Log Out":
            st.success("Log Out Successful!")  
            st.session_state.admin_logged_in = False
    else:
        admin_login()

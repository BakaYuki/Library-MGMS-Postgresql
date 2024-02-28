from dbconnection import *
from addbook import *
from admin import *
from issuebook import *
from student import *

def main():
    st.title("Library Management System")
    #User Selection
    
    user_type = st.sidebar.selectbox("Select User Type", ["User", "Admin"])

    #Student Panel
    if user_type == "User":
        student_panel()
    
    #Admin Panel
    elif user_type == "Admin":
        if 'admin_logged_in' not in st.session_state:
            st.session_state.admin_logged_in = False
        admin_login()
    admin_panel()

if __name__ == "__main__":
    main()
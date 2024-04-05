from dbconnection import *
from addbook import *
from admin import *
from issuebook import *
from student import *

def main():
    # st.title("Library Management System")
    #User Selection
    # user_type = st.sidebar.selectbox("Select User Type", ["User", "Admin"])
    # user_type = "Admin"


    # Adding a header
    st.header("Welcome to Library Management System 📖")

    # User Selection
    user_type = st.sidebar.selectbox("Select User Type", ["User", "Admin"])

   # Custom styling header
    st.markdown(
        """
        <style> 
            h2 {
                color:  #00ffff;
            }
            h3 {
                color:  #3498db;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    


    # st.write(user_type)
    
    #Student Panel
    if user_type == "User":
    # Display a welcome message based on the user type
        st.success("Welcome, User! Explore our collection and borrow books.")
        student_panel()
    
    #Admin Panel
    elif user_type == "Admin":
        st.success("Welcome, Admin! Manage the library and books.")
        if 'admin_logged_in' not in st.session_state:
            st.session_state.admin_logged_in = False
            admin_login()
        else:
            admin_panel()

if __name__ == "__main__":
    main()
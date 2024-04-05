from dbconnection import *
from registration import *
from addproduct import *
from updateproduct import *

def login():
    st.subheader("Login",divider="red")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    password = hash_password(password)  
    # st.markdown("Forgot your password? [Reset here](http://localhost:8502/register)")                                                                                    
    
    if st.button("Login"):
        user = get_user_by_username(username)
        if user:
            if password == user[2]:
                st.success("Login successful!")
                st.write(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.user = user
            else:
                st.session_state.logged_in = False
                st.error("Invalid password. Please try again.")
        else:
            st.error("User does not exist. Please register.")

    st.subheader("OR ")
    if st.button(r"$\textsf{\large Create Account}$"):
        st.session_state.initial = False
        
def admin_panel():
    
    if st.session_state.get('logged_in', True):
        # st.title("Admin Panel")
        admin_option = st.sidebar.selectbox("Choose Option", ["Add Product", "Update Product", "View Product", "Log Out"])
        
        if admin_option == "Add Product": 
            add_product()

        elif admin_option == "Update Product":
            update_product()
          
            
        elif admin_option == "View Product":
            view_products()  

         

        elif admin_option == "Log Out":
            st.success("Log Out Successful!")  
            st.session_state.admin_logged_in = False
    else:
        login()
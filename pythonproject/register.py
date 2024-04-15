from dbconn import *

def register():
    st.subheader("Register New User")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    if st.button("Register"):
        if get_user_by_username(new_username):
            st.warning("User already exists. Please choose another username.")
        else:
            add_user(new_username, new_password)
            st.success("User registered successfully!")
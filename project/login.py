from dbconn import *

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user_by_username(username)
        if user:
            if password == user[2]:
                st.success("Login successful!")
                st.write(f"Welcome, {username}!")
            else:
                st.error("Invalid password. Please try again.")
        else:
            st.error("User does not exist. Please register.")

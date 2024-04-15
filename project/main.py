from dbconn import *
from register import *
from login import *



def add_password(user_id, website, username, password):

    cur.execute("INSERT INTO passwords (user_id, website, username, password) VALUES (%s, %s, %s, %s)",
                (user_id, website, username, password))
    conn.commit()

# Streamlit UI
def main():
    st.title("Password Manager")
    """
    # Create user and password tables if not exists
    create_user_table()
    create_password_table()
    """

    menu = ["Register", "Login", "Add Password", "View Passwords"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        register()

    elif choice == "Login":
        login()
        
        
"""    elif choice == "Add Password":
        st.subheader("Add New Password")
        website = st.text_input("Website")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Add"):
            # Here, you would need to authenticate the user and get their user_id
            # For demonstration, I'm using a placeholder user_id of 1
            add_password(1, website, username, password)
            st.success("Password added successfully!")

    elif choice == "View Passwords":
        st.subheader("View Passwords")
        # Here, you would need to authenticate the user and get their user_id
        # For demonstration, I'm using a placeholder user_id of 1
        passwords = get_passwords_by_user_id(1)
        if passwords:
            for password in passwords:
                st.write(f"Website: {password[2]}, Username: {password[3]}, Password: {password[4]}")
        else:
            st.write("No passwords stored yet.")
"""
if __name__ == '__main__':
    main()

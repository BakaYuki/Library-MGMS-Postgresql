from dbconn import *

def get_user_by_username(username):
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    return user

# Function to add a new user
def add_user(username, password):
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password))
    conn.commit()
    
def main():
    st.title("Password Manager")

    st.sidebar.title("Menu")
    menu_option = st.sidebar.selectbox("Select Option", ["Register", "Login"])

    if menu_option == "Register":
        st.subheader("Register New User")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        if st.button("Register"):
            if get_user_by_username(new_username):
                st.warning("User already exists. Please choose another username.")
            else:
                add_user(new_username, new_password)
                st.success("User registered successfully!")

    elif menu_option == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = get_user_by_username(username)
            if user:
                if password == user[2]:
                    st.success("Login successful!")
                    st.write(f"Welcome, {username}!")

                    # Display Add Password and View Passwords options after successful login
                    st.sidebar.subheader("Options")
                    selected_option = st.sidebar.selectbox("Select Option", ["Add Password", "View Passwords"])

                    if selected_option == "Add Password":
                        st.subheader("Add New Password")
                        website = st.text_input("Website")
                        username = st.text_input("Username")
                        password = st.text_input("Password", type="password")
                        if st.button("Add"):
                            # add_password(user[0], website, username, password)
                            st.success("Password added successfully!")

                    elif selected_option == "View Passwords":
                        st.subheader("View Passwords")
                        # passwords = get_passwords_by_user_id(user[0])
                        passwords = True
                        if passwords:
                            for password in passwords:
                                st.write(f"Website: {password[2]}, Username: {password[3]}, Password: {password[4]}")
                        else:
                            st.write("No passwords stored yet.")

                else:
                    st.error("Invalid password. Please try again.")
            else:
                st.error("User does not exist. Please register.")

if __name__ == '__main__':
    main()
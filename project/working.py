from dbconn import *


# Function to add a new user
def add_user(username, password):

    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password))
    conn.commit()
    conn.close()

# Function to retrieve user by username
def get_user_by_username(username):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    conn.close()
    return user

# Function to add a new password
def add_password(user_id, website, username, password):

    cur = conn.cursor()
    cur.execute("INSERT INTO passwords (user_id, website, username, password) VALUES (%s, %s, %s, %s)",
                (user_id, website, username, password))
    conn.commit()
    conn.close()

# Function to retrieve passwords by user_id
def get_passwords_by_user_id(user_id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords WHERE user_id = %s", (user_id,))
    passwords = cur.fetchall()
    conn.close()
    return passwords

# Streamlit UI
def main():
    st.title("Password Manager")


    menu = ["Register", "Login", "Add Password", "View Passwords"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Register":
        st.subheader("Register New User")
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type="password")
        if st.button("Register"):
            if get_user_by_username(new_username):
                st.warning("User already exists. Please choose another username.")
            else:
                add_user(new_username, new_password)
                st.success("User registered successfully!")

    elif choice == "Login":
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

    elif choice == "Add Password":
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

if __name__ == '__main__':
    main()

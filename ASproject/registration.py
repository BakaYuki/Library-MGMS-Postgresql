import hashlib
from dbconnection import *

def registration_form():
     # User Registration Form
        st.subheader("User Registration",divider="red")
        reg_username = st.text_input("Username:")
        reg_password = st.text_input("Password:", type="password")
        if st.button("Register"):
            if reg_username and reg_password:
                register_user(conn, reg_username, reg_password)
                st.success("Registration successful!")
            else:
                st.error("Please enter both username and password.")
        if st.button("Go back to Login"):
            st.session_state.initial = True

# # Function to add a new user
# def add_user(username, password):
#     cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
#                 (username, password))
#     conn.commit()

# Hashing Function for password ( one way hash )                
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_username(username):
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    return user


# Function to register a new user
def register_user(conn, username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cur.execute("""
        INSERT INTO users (username, password)
        VALUES (%s, %s)
    """, (username, hashed_password))
    conn.commit()

if __name__ == '__main__':
    registration_form()
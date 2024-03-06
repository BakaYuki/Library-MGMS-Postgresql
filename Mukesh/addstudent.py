from dbconnection import *

def add_student():
    st.subheader("Add Student")
    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")
    student_email = st.text_input("Student Email")
    if st.button("Add Student"):
        
        try:
            cur.execute(
                "INSERT INTO student (student_id,name,email) VALUES (%s, %s, %s)",
                (student_id, student_name, student_email)
            )
            conn.commit()
            st.success("Student added successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding student: {e}")
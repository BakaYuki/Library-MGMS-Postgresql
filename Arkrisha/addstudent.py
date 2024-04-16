from dbconnection import *

def add_student():
    st.subheader("Add Student")
    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")
    student_email = st.text_input("Student Email")
    if st.button("Add Student"):
        if not student_id or not student_name or not student_email:
            st.error("Please fill in all fields.")
            return
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
    delete_checked = st.checkbox("Delete Student")
    try:
        if delete_checked:
            confirm_delete = st.button("Confirm Delete")
            if confirm_delete:
                if not student_id:
                    st.error("Please enter a student ID.")
                    return
                # Check if the student exists before deleting
                cur.execute("SELECT * FROM student WHERE student_id = %s", (student_id,))
                existing_student = cur.fetchone()
                if existing_student:
                    # Delete the student from the database
                    cur.execute("DELETE FROM student WHERE student_id = %s", (student_id,))
                    conn.commit()
                    st.success("Student details deleted successfully!")  
                else:
                    st.error("Student with provided ID does not exist.")
    except psycopg2.Error:
        conn.rollback()
        st.error("Student has books issued.")          
           
            
def view_student():
    try :
        cur.execute("SELECT * FROM student ")
        student_list = cur.fetchall()
        # Display students in a table
        table_data = [("ID", "Name", "Email")]
        for student in student_list:
            table_data.append((student[0], student[1], student[2]))
        st.table(table_data)

    except psycopg2.Error as e:
        st.error(f"Error searching for product: {e}")    
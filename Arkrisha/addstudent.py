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
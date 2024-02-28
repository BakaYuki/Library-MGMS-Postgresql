from dbconnection import *
from issuebook import *
from returnbook import *
def student_panel():
    student_option = st.sidebar.selectbox("Choose Option", ["Issue Book", "Return Book"])
    
    if student_option == "Issue Book":
        issue_book()
        
    elif student_option == "Return Book":
        return_book()
        # st.write("Return book functionality goes here")
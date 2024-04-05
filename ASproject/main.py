from dbconnection import *
from registration import *
from addproduct import *
from login import *

def main():
    # header()
    st.header("Product Stock Manager",divider='blue')
    if 'initial' not in st.session_state:
        st.session_state.initial = True
        st.session_state.logged_in = False
    
    if st.session_state.initial==True:
        admin_panel()
    else:
        registration_form()
        
if __name__ == '__main__':
    main()
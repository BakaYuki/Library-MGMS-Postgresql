from dbconnection import *

def update_product():   
    user_id =  st.session_state.user[0]
    st.subheader("Update Product")
    #Session State hold the product_id entered by the user even after page refresh
    st.session_state.product_id = st.text_input("Enter the Product ID:")
    product_id = st.session_state.product_id
    
    # Initialize Button Clicked state to False during starting
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False
    
    #Session State to True when button is clicked so that the product information can be displayed and updated
    if st.button("Update Product Detail"):
        st.session_state.button_clicked = True
    
    # If the button is clicked, retrieve the product information from the database
    if st.session_state.button_clicked: 
        # Check if product_id is not empty
        if product_id.strip(): 
            # Convert product_id to integer
            product_id = int(product_id)
            # Retrieve product information from the database
            cur.execute("SELECT * FROM products WHERE product_id = %s and user_id = %s", (product_id,user_id,))
            product = cur.fetchone()
            
            #Display the product information in the form
            if product:
                # product_id, name, price, stock_quantity
                product_id = product[0]
                name = product[1]
                price = product[2]
                stock_quantity = product[3]
                categories = product[5]
                #Product ID displayed only and cannot be changed
                st.write(f"Product ID: {product_id}")
                #value = shows the current information from the database
                name = st.text_input("Product Name", value=name) 
                price = st.text_input("Price", value=price)
                stock_quantity = st.text_input("Quantity", value=stock_quantity)
                categories = st.text_input("Category", value=categories)
                if st.button("Save Changes"):
                    # Update the product information in the database
                    try:
                        cur.execute(
                            "UPDATE products SET name = %s, price = %s, stock_quantity = %s, categories = %s WHERE product_id = %s",
                            (name, price, stock_quantity, categories, product_id)
                        )
                        conn.commit()
                        st.success("Product updated successfully!")
                    except psycopg2.Error as e:
                        conn.rollback()
                        st.error(f"Error updating product: {e}")
                        
                # Add a delete button
                delete_checked = st.checkbox("Delete Product")
                if delete_checked:
                    confirm_delete = st.button("Confirm Delete")
                    if confirm_delete:
                        # Delete the product from the database
                        cur.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
                        conn.commit()
                        st.success("Product deleted successfully!")
                        
            else:
                st.error("No such product found")
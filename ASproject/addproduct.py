from dbconnection import *

'''# Function to create a table for products if it doesn't exist
def create_product_table(conn):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    """)
    conn.commit()'''

# Function to add a new product to the database
def add_product():
    st.subheader("Add New Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price",min_value=0.0,step=10.0)
    stock_quantity = st.number_input("Quantity",min_value=0,step=5)
    user_id =  st.session_state.user[0]
    # Retrieve previously input categories from the database
    cur.execute("SELECT DISTINCT categories FROM products WHERE user_id = %s", (user_id,))
    previous_categories = [row[0] for row in cur.fetchall()]
    
    # Allow users to input categories
    categories = st.text_input("Enter categories")
    categories_list = [category.strip() for category in categories.split(",")] if categories else []
    
    st.write("OR")
    
    # Display previously input categories with a dropdown arrow for selection
    if previous_categories:
        selected_categories = st.multiselect("Select categories", previous_categories)
        # Add the selected categories to the categories list
        categories_list.extend(selected_categories)
        
    if st.button("Add"):
        try:
            cur.execute("""
                INSERT INTO products (name, price, stock_quantity,categories,user_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, price, stock_quantity,",".join(categories_list),user_id))
            conn.commit()
            st.success("Added Successfully")
            
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding product: {e}")

    
# Function to retrieve all products from the database
def view_products():
    user_id =  st.session_state.user[0]
    try :
        cur.execute("SELECT * FROM products WHERE user_id = %s",(user_id,))
        product_list = cur.fetchall()
        # Display products in a table
        table_data = [("ID", "Product Name", "Price", "Quantity", "Category")]
        for product in product_list:
            table_data.append((product[0], product[1], product[2], product[3], product[5]))
        st.table(table_data)

    except psycopg2.Error as e:
        st.error(f"Error searching for product: {e}")



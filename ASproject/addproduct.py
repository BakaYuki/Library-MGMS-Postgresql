from dbconnection import *
# from login import *

# Function to create a table for products if it doesn't exist
def create_product_table(conn):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL,
            stock_quantity INTEGER NOT NULL
        )
    """)
    conn.commit()

# Function to add a new product to the database
def add_product():
    st.subheader("Add New Product")
    name = st.text_input("Product Name")
    price = st.text_input("Price")
    stock_quantity = st.text_input("Quantity")
    user_id =  st.session_state.user[0]
    if st.button("Add"):
        try:
            cur.execute("""
                INSERT INTO products (name, price, stock_quantity,user_id)
                VALUES (%s, %s, %s,%s)
            """, (name, price, stock_quantity,user_id))
            conn.commit()
            st.success("Added Successfully")
        except psycopg2.Error as e:
            conn.rollback()
            st.error(f"Error adding product: {e}")

# Function to retrieve all products from the database
def view_products():
    try :
        cur.execute("SELECT * FROM products")
        product_list = cur.fetchall()
        # Display products in a table
        table_data = [("ID", "Product Name", "Price", "Quantity")]
        for product in product_list:
            table_data.append((product[0], product[1], product[2], product[3]))
        st.table(table_data)

    except psycopg2.Error as e:
        st.error(f"Error searching for product: {e}")



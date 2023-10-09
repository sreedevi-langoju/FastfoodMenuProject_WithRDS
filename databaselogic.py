import mysql.connector

#Establish a database connection
def connectdatabase():
    # Database configuration
    db_config = {
    'host': 'endpoint', # provide the RDS endpoint
    'user': 'user',# provide your database user name 
    'password': 'xx', # provide your database password
    'database': 'fastfood' # provide your database name
    }

    # database connection
    connection = mysql.connector.connect(**db_config)
    return connection

def openCursor(connection):
    cursor = connection.cursor()
    return cursor

def closeAll(cursor,connection):
    cursor.close()
    connection.close()
  

def get_menu_from_database():
    try:
        connection=connectdatabase()
        cursor=openCursor(connection)
        # Execute the SQL query to fetch menu data
        query = "SELECT Item_Num, Item_Name, Price, Image FROM Menu"
        cursor.execute(query)

        # Fetch all the rows as a list of tuples
        menu_data = cursor.fetchall()

        # Process the menu data and create the menu dictionary
        menu = {}
        for row in menu_data:
            Item_Num, name, price, image = row
            menu[str(Item_Num)] = {'name': name, 'price': float(price), 'image': image}

        return menu

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        closeAll(cursor,connection)


def insert_order(order_date,total_cost):
    connection=connectdatabase()
    cursor=openCursor(connection)
    # Use prepared statements to insert the order into the database with the order date
    insert_orders_query = "INSERT INTO Orders (Order_Date, Total_Cost) VALUES (%s,%s)"
    orders_values = (order_date,total_cost)
    try:
        cursor.execute(insert_orders_query, orders_values)
        connection.commit()
        # Retrieve the generated order_num
        order_num = cursor.lastrowid
        return order_num
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        closeAll(cursor,connection)

def insert_orders_details(item_name, quantity, price, order_date,total_cost,order_num):
    connection=connectdatabase()
    cursor=openCursor(connection)
    # Use prepared statements to insert the order into the database with the order date
    insert_orders_details_query = "INSERT INTO Orders_Details (Order_Num,Order_Date,Item_Name,Price, Quantity) VALUES (%s, %s, %s, %s, %s)"
    orders_details_values = (order_num,order_date,item_name,price,quantity)
    try:
        cursor.execute(insert_orders_details_query,orders_details_values)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        closeAll(cursor,connection)

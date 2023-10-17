import mysql.connector
from dbconnection import connect_database

def openCursor(connection):
    cursor = connection.cursor()
    return cursor

def closeAll(cursor, connection):
    cursor.close()
    connection.close()

def initialize_connection_and_cursor():
    connection = None
    cursor = None

    try:
        connection = connect_database()
        cursor = openCursor(connection)
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    
    return connection, cursor

def get_menu_from_database():
    connection, cursor = initialize_connection_and_cursor()
    print("Connection successful in database logic")
    
    try:
        query = "SELECT Item_Num, Item_Name, Price, Image FROM Menu"
        cursor.execute(query)  # Execute the query
        
        menu_data = cursor.fetchall()
        print("Fetching the menu_data in database logic")
        
        menu = {}
        for row in menu_data:
            Item_Num, name, price, image = row
            menu[str(Item_Num)] = {'name': name, 'price': float(price), 'image': image}
            print("Menu data name in the for loop in database logic is", name)
        return menu
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        closeAll(cursor, connection)

def insert_order(order_date, total_cost):
    connection, cursor = initialize_connection_and_cursor()

    try:
        query = "INSERT INTO Orders (Order_Date, Total_Cost) VALUES (%s, %s)"
        values = (order_date, total_cost)
        cursor.execute(query, values)
        order_num = cursor.lastrowid
        connection.commit()
        return order_num

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

def insert_orders_details(item_name, quantity, price, order_date, total_cost, order_num):
    connection, cursor = initialize_connection_and_cursor()

    try:
        query = "INSERT INTO Orders_Details (Order_Num, Order_Date, Item_Name, Price, Quantity) VALUES (%s, %s, %s, %s, %s)"
        values = (order_num, order_date, item_name, price, quantity)
        cursor.execute(query, values)
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")

if __name__ == '__main__':
    from dbconnection import connect_database

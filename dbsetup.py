import mysql.connector
from dbconnection import connect_database

def initialize_connection_and_cursor():
    connection = None
    cursor = None

    try:
        connection = connect_database()
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    
    return connection, cursor

def close_connection_and_cursor(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()

def setup_database():
    connection, cursor = initialize_connection_and_cursor()

    if connection and cursor:
        try:
            # Attempt to create the 'Menu' table only if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Menu (
                    Item_Num INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    Item_Name VARCHAR(25) NOT NULL,
                    Price DECIMAL(10, 2) NOT NULL,
                    Image VARCHAR(25)
                )
            """)

            # Attempt to create the 'Orders' table only if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    Order_Num INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    Order_Date DATE,
                    Total_Cost DECIMAL(10, 2)
                )
            """)

            # Attempt to create the 'Orders_Details' table only if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders_Details (
                    Order_Detail_Num INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    Order_Date DATE,
                    Item_Name VARCHAR(25) NOT NULL,
                    Price DECIMAL(10, 2) NOT NULL,
                    Quantity INT,
                    Order_Num INT NOT NULL,
                    FOREIGN KEY (Order_Num) REFERENCES Orders(Order_Num)
                )
            """)

            # Attempt to fetch data from the 'Menu' table
            cursor.execute("SELECT COUNT(*) FROM Menu")
            num_rows = cursor.fetchone()[0]

            # If no data exists, insert data into the 'Menu' table
            if num_rows == 0:
                # Insert data into the 'Menu' table
                menu_data = [
                    ('Hamburger', 5.99, 'Hamburger.jpeg'),
                    ('Cheeseburger', 6.49, 'Cheeseburger.jpeg'),
                    ('Chicken Sandwich', 7.99, 'Chicken_sandwich.jpeg'),
                    ('French Fries', 2.49, 'Frenchfries.jpeg'),
                    ('Soda', 1.49, 'Soda.jpeg')
                ]

                for item in menu_data:
                    cursor.execute("INSERT INTO Menu (Item_Name, Price, Image) VALUES (%s, %s, %s)", item)

            # Similar logic for inserting data into 'Orders' and 'Orders_Details' tables

            connection.commit()
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        finally:
            close_connection_and_cursor(connection, cursor)

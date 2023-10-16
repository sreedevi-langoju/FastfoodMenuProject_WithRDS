# Setup the database schema with required tables and data
import mysql.connector
from dbconnection import connect_database  # Import the connect_database function from db_connection.py

def setup_database():
    connection = connect_database()  # Call the connect_database function from db_connection.py
    cursor = connection.cursor()

    # Create the 'Menu' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Menu (
            Item_Num INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Item_Name VARCHAR(25) NOT NULL,
            Price DECIMAL(10, 2) NOT NULL,
            Image VARCHAR(25)
        )
    """)

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

    # Create the 'Orders' table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            Order_Num INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            Order_Date DATE,
            Total_Cost DECIMAL(10, 2)
        )
    """)

    # Create the 'Orders_Details' table
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

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    from dbconnection import connect_database
    setup_database()

from flask import Flask, render_template, request, redirect, url_for
import databaselogic
import datetime
import logging

app = Flask(__name__)

menu = databaselogic.get_menu_from_database()
logging.info(f"Menu data: {menu}")
order = {}
#order_num = 0  # Define order_num as a global variable and initialize it to 0

@app.route('/', methods=['GET', 'POST'])
def place_order():
    global order_num  # Use a global variable for order_num
    if request.method == 'POST':
        order_date = datetime.datetime.now()  # Get the current date and time
        for item_num, quantity in request.form.items():
            if item_num.startswith('quantity_'):
                item_num = item_num.replace('quantity_', '')
                try:
                    quantity = int(quantity)
                    if quantity <= 0:
                        continue
                    
                    if item_num in menu:
                        if item_num in order:
                            order[item_num]['quantity'] += quantity
                        else:
                            order[item_num] = {'name': menu[item_num]['name'], 'price': menu[item_num]['price'], 'quantity': quantity}
                        
                       
                except ValueError:
                    print("Invalid Quantity Value")

        total_cost = round(calculate_total(order), 2)
        #order_num += 1  # Increment order_num for each new order
        # Insert the order into the MariaDB database tables
        insert_data(order_date, total_cost, menu, request.form)
        return render_template('receipt.html', order=order, total_cost=total_cost)
    
    return render_template('index.html', menu=menu)

def calculate_total(order):
    total = 0
    for item_info in order.values():
        total += item_info['price'] * item_info['quantity']
    return total

def insert_data(order_date, total_cost, menu, form_data):
    # Insert the order into the "orders" table and retrieve the generated order_num
    order_num = databaselogic.insert_order(order_date, total_cost)

    for item_key, quantity in form_data.items():
        if item_key.startswith('quantity_'):
            item_num = item_key.replace('quantity_', '')  # Extract the item number from the key
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    continue

                if item_num in menu:
                    # Use the same order_num in the "Orders_details" table
                    databaselogic.insert_orders_details(menu[item_num]['name'], quantity, menu[item_num]['price'], order_date, total_cost, order_num)
            except ValueError:
                print("Invalid Quantity Value")

if __name__ == '__main__':
    app.run(debug=True)


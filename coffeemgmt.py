import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="pass123",  # Replace with your MySQL password
    database="brewhub"
)

cursor = db.cursor()


# Function to capture customer details
def capture_customer_details():
    name = input("Enter your name: ")
    contact_number = input("Enter your contact number: ")
    email = input("Enter your email: ")

    # Insert into Customers table
    sql = "INSERT INTO Customers (name, contact_number, email) VALUES (%s, %s, %s)"
    values = (name, contact_number, email)
    cursor.execute(sql, values)
    db.commit()
    return cursor.lastrowid  # Return customer_id

# Function to display main menu and handle customer choice
def display_main_menu():
    print("Main Menu:")
    print("1. Coffees")
    print("2. Iced Teas & Lemonades")
    print("3. Milkshakes")
    print("4. Snacks")
    choice = input("Enter your choice (1-4) (0 to finish): ")
    return int(choice)

# Function to display product menu based on category
def display_product_menu(category):
    sql = "SELECT product_id, item, price FROM Products WHERE category = %s"
    cursor.execute(sql, (category,))
    products = cursor.fetchall()
    
    print(f"{category} Menu:")
    print("pro_id | item                 | price")
    print("----------------------------------------")
    for product in products:
        print(f"{product[0]}      | {product[1]:<20} | Rs. {product[2]:.2f}")
    print("----------------------------------------")
    return products

# Function to take orders from the customer
def take_orders(customer_id):
    order_items = []
    while True:
        category_choice = display_main_menu()
        if category_choice == 0:
            break
        
        categories = {
            1: "Coffees",
            2: "Iced Teas & Lemonades",
            3: "Milkshakes",
            4: "Snacks"
        }
        chosen_category = categories.get(category_choice)
        if chosen_category:
            products = display_product_menu(chosen_category)
            
            while True:
                try:
                    product_id = int(input("Enter product ID to order (0 to finish): "))
                    if product_id == 0:
                        break
                    selected_product = next((p for p in products if p[0] == product_id), None)
                    if not selected_product:
                        print("Invalid product ID. Please enter a valid product ID.")
                        continue
                    
                    quantity = int(input(f"How many {selected_product[1]} do you want? "))
                    if quantity <= 0:
                        print("Invalid quantity. Please enter a valid quantity.")
                        continue
                    
                    order_items.append({
                        "product_id": product_id,
                        "quantity": quantity,
                        "price": selected_product[2]
                    })
                    
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
    place_order(customer_id, order_items)

# Function to place order in the database
def place_order(customer_id, order_items):
    try:
        # Insert into Orders table
        total_amount = sum(item['quantity'] * item['price'] for item in order_items)
        sql_order = "INSERT INTO Orders (customer_id, total_amount) VALUES (%s, %s)"
        values_order = (customer_id, total_amount)
        cursor.execute(sql_order, values_order)
        order_id = cursor.lastrowid
        
        # Insert into Order_Items table
        for item in order_items:
            sql_order_item = "INSERT INTO Order_Items (order_id, product_id, quantity, item_price) VALUES (%s, %s, %s, %s)"
            values_order_item = (order_id, item['product_id'], item['quantity'], item['price'])
            cursor.execute(sql_order_item, values_order_item)
        
        db.commit()
        
        # Generate and display bill receipt
        generate_bill(order_id)
        
    except mysql.connector.Error as error:
        print(f"Error placing order: {error}")

# Function to generate and display bill receipt
# Function to generate and display bill receipt
# Function to generate and display bill receipt
def generate_bill(order_id):
    try:
        # Fetch order details
        sql_order = "SELECT Orders.order_id, Customers.name, Customers.contact_number, Customers.email, Orders.total_amount FROM Orders JOIN Customers ON Orders.customer_id = Customers.customer_id WHERE Orders.order_id = %s"
        cursor.execute(sql_order, (order_id,))
        order_info = cursor.fetchone()

        # Fetch order items
        sql_items = "SELECT Products.item, Order_Items.quantity, Order_Items.item_price FROM Order_Items JOIN Products ON Order_Items.product_id = Products.product_id WHERE Order_Items.order_id = %s"
        cursor.execute(sql_items, (order_id,))
        order_items = cursor.fetchall()

        # Display bill receipt
        
        print("\n****************** Bill Receipt ******************")
        print("\n")
        print("                BrewHub                 ")
        print("   Crafting Moments, One Brew at a Time! ")
        print(" ")
        print(f"Order ID: {order_info[0]}")
        print(f"Customer Name: {order_info[1]}")
        print(f"Contact Number: {order_info[2]}")
        print(f"Email: {order_info[3]}")
        print("--------------------------------------------------")
        print("Ordered Items:")
        print("Item                      Quantity   Price")
        print("--------------------------------------------------")
        subtotal = 0.0  # Initialize subtotal as float

        for item in order_items:
            item_name = item[0]
            quantity = item[1]
            item_price = float(item[2])  # Convert item_price to float
            total_price = quantity * item_price
            print(f"{item_name:<25} {quantity:<10} Rs. {total_price:.2f}")
            subtotal += total_price  # Accumulate subtotal

        print("--------------------------------------------------")
        print("\n")
        tax = subtotal * 0.02  # Assuming 2% GST
        total_amount = subtotal + tax

        print(f"Subtotal: Rs. {subtotal:.2f}")
        print(f"Tax (GST 2%): Rs. {tax:.2f}")
        print("--------------------------------------------------")
        print(f"Total Amount: Rs. {total_amount:.2f}")
        print("--------------------------------------------------")
        print("\n------------------ BrewHub -----------------------")
        print("\n-------------- Have A Nice Day!! -----------------")
        print("\n****************** Thank You *********************")
        print("\n")

    except mysql.connector.Error as error:
        print(f"Error generating bill: {error}")



# Main function to run the coffee shop management system
def main():
    try:
        customer_id = capture_customer_details()
        take_orders(customer_id)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        db.close()

# Execute the main function
if __name__ == "__main__":
    main()

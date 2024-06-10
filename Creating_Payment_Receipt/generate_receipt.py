import os  # For verifying ReportLab installation
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

def generate_transaction_receipt(data):
    """
    Creates a PDF receipt using the ReportLab library.

    Args:
        data (dict): Contains receipt details including:
            - 'store_name' (str): The name of the store.
            - 'customer_name' (str): The customer's name.
            - 'date' (str): The transaction date.
            - 'items' (list): A list of dictionaries for each item with:
                - 'name' (str): The item name.
                - 'quantity' (int): The quantity purchased.
                - 'price' (float): The price per unit.
            - 'subtotal' (float): The pre-tax total.
            - 'tax_rate' (float): The tax rate (e.g., 0.07 for 7%).
            - 'tax_amount' (float): The calculated tax amount.
            - 'total' (float): The final total including tax.
    """
    pass

def get_receipt_details():
    store_name = input("Enter the store name: ")
    customer_name = input("Enter the customer name: ")
    date_str = input("Enter the date (DD-MM-YYYY): ")

    # Parse the input date and format it as 'DD-MM-YYYY'
    parsed_date = datetime.strptime(date_str, '%d-%m-%Y')
    formatted_date = parsed_date.strftime('%d-%m-%Y')

    items = []
    while True:
        item_name = input("Enter the item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Enter the quantity for {item_name}: "))
        price = float(input(f"Enter the price for {item_name}: "))
        items.append({"name": item_name, "quantity": quantity, "price": price})

    subtotal = sum(item['quantity'] * item['price'] for item in items)
    tax_rate = 0.05  # Example tax rate of 5%
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    receipt_data = {
        "store_name": store_name,
        "customer_name": customer_name,
        "date": formatted_date,
        "items": items,
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total": total
    }

    return receipt_data

if __name__ == "__main__":
    receipt_info = get_receipt_details()
    generate_transaction_receipt(receipt_info)

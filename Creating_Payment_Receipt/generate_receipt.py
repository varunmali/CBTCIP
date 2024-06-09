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
    pass

if __name__ == "__main__":
    receipt_info = get_receipt_details()
    generate_transaction_receipt(receipt_info)

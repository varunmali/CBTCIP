# Creating Payment Receipt

This project is a simple transaction receipt generator using Python and the ReportLab library. It allows users to input transaction details and generates a PDF receipt.

## Features

- Collects transaction details from the user.
- Generates a PDF receipt with itemized transaction details, subtotal, tax, and total amount.
- Uses the ReportLab library to create PDF documents.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/varunmali/CBTCIP.git
   cd CBTCIP/Creating_Payment_Receipt
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required package:

   ```bash
   pip install reportlab
   ```

## Usage

Run the script and follow the prompts to enter transaction details. The script will generate a PDF receipt.

```bash
python generate_receipt.py
```

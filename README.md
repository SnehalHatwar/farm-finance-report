Farm Finance Report Generator

# Overview
The project is a simple Flask backend that takes farm finance information from a web form, gives a financial summary, draws a graph, and even makes a PDF report that can be saved.

# Features
- Easy HTML form
- Income/expense rows can be added in multiple numbers
- Chart of Income minus Expenses
- PDF creation done automatically
- Ledger created automatically
- Clean and easy-to-understand structure with the utils/ folder

# Setup Instructions
1. Repository cloning.
2. A virtual environment to be created.
3. Installing requirements:
   pip install -r requirements.txt
4. Running the app:
   python app.py

# How to Use the Application
1.Open the web form.
2.Enter the details of the farmer and crop.
3.As many income and expense rows as needed can be added.
4.Submit the form to get the PDF.
5.Get the PDF report and see it.

# Libraries Used
- Flask
- ReportLab
- Matplotlib
- Pandas

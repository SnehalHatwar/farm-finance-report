from flask import Flask, render_template, request, send_file
import os
from utils.pdf_generator import generate_pdf
from utils.charts import create_summary_chart
import pandas as pd
from datetime import datetime
import webbrowser
import threading

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/generate", methods=["POST"])
def generate():
    farmer = request.form["farmer"]
    crop = request.form["crop"]
    season = request.form["season"]
    acres = float(request.form["acres"])
    sow = request.form["sowing"]
    harvest = request.form["harvest"]
    location = request.form["location"]

    # Process Expense rows
    expense_categories = request.form.getlist("expense_category")
    expense_amounts = request.form.getlist("expense_amount")
    expense_dates = request.form.getlist("expense_date")
    expense_desc = request.form.getlist("expense_desc")

    expenses = []
    for i in range(len(expense_categories)):
        if expense_categories[i].strip() != "":
            expenses.append({
                "Category": expense_categories[i],
                "Amount": float(expense_amounts[i]),
                "Date": expense_dates[i],
                "Description": expense_desc[i]
            })

    # Process Income rows
    income_categories = request.form.getlist("income_category")
    income_amounts = request.form.getlist("income_amount")
    income_dates = request.form.getlist("income_date")
    income_desc = request.form.getlist("income_desc")

    incomes = []
    for i in range(len(income_categories)):
        if income_categories[i].strip() != "":
            incomes.append({
                "Category": income_categories[i],
                "Amount": float(income_amounts[i]),
                "Date": income_dates[i],
                "Description": income_desc[i]
            })

    total_expense = sum(x["Amount"] for x in expenses)
    total_income = sum(x["Amount"] for x in incomes)
    profit_loss = total_income - total_expense
    cost_per_acre = total_expense / acres

    # Make chart
    chart_path = create_summary_chart(total_income, total_expense)

    # Generate final PDF
    filename = f"{crop}_{acres}_{season}_{datetime.now().year}.pdf"
    pdf_path = generate_pdf(
        farmer, crop, season, acres, sow, harvest, location,
        expenses, incomes,
        total_income, total_expense, profit_loss, cost_per_acre,
        chart_path, filename
    )

    return send_file(pdf_path, as_attachment=True)


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    # Open browser after server starts in a separate thread
    threading.Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)


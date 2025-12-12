from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from reportlab.lib import colors

def generate_pdf(farmer, crop, season, acres, sow, harvest, location,
                 expenses, incomes,
                 total_income, total_expense, profit_loss, cost_per_acre,
                 chart_path, filename):

    pdf = SimpleDocTemplate(filename, pagesize=A4)
    style = getSampleStyleSheet()["Normal"]
    story = []

    # HEADER
    story.append(Paragraph(f"<b>GramIQ Report</b>", style))
    story.append(Paragraph(f"Report: {crop}_{acres}_{season}_{datetime.now().year}", style))
    story.append(Paragraph(f"Farmer: {farmer}", style))
    story.append(Paragraph(f"Generated: {datetime.now()}", style))
    story.append(Spacer(1, 20))

    # SUMMARY
    story.append(Paragraph("<b>Finance Summary</b>", style))
    story.append(Paragraph(f"Total Income: {total_income}", style))
    story.append(Paragraph(f"Total Expense: {total_expense}", style))
    story.append(Paragraph(f"Profit / Loss: {profit_loss}", style))
    story.append(Paragraph(f"Cost per Acre: {cost_per_acre}", style))
    story.append(Spacer(1, 10))

    # CHART
    story.append(Image(chart_path, width=300, height=200))
    story.append(Spacer(1, 20))

    # EXPENSE TABLE
    story.append(Paragraph("<b>Expense Breakdown</b>", style))
    expense_data = [["Category", "Amount", "Date", "Description"]] + [
        [e["Category"], e["Amount"], e["Date"], e["Description"]] for e in expenses
    ]
    story.append(Table(expense_data))
    story.append(Spacer(1, 20))

    # INCOME TABLE
    story.append(Paragraph("<b>Income Breakdown</b>", style))
    income_data = [["Category", "Amount", "Date", "Description"]] + [
        [i["Category"], i["Amount"], i["Date"], i["Description"]] for i in incomes
    ]
    story.append(Table(income_data))
    story.append(Spacer(1, 20))

    # LEDGER
    story.append(Paragraph("<b>Ledger</b>", style))
    ledger = [["Date", "Particulars", "Type", "Description", "Amount"]]

    for e in expenses:
        ledger.append([e["Date"], e["Category"], "Expense", e["Description"], e["Amount"]])

    for i in incomes:
        ledger.append([i["Date"], i["Category"], "Income", i["Description"], i["Amount"]])

    story.append(Table(ledger))
    story.append(Spacer(1, 20))

    # FOOTER
    story.append(Paragraph("<center>Proudly maintained accounting with GramIQ</center>", style))

    pdf.build(story)

    return filename

import matplotlib.pyplot as plt

def create_summary_chart(income, expense):
    labels = ["Income", "Expense"]
    values = [income, expense]

    plt.figure(figsize=(4, 3))
    plt.bar(labels, values)
    plt.title("Income vs Expense")
    path = "summary_chart.png"
    plt.savefig(path)
    plt.close()
    return path

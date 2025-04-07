from datetime import datetime

expenses = []

def add_expense(date, amount, category, description):
    try:
        expense_date = datetime.strptime(date, "%Y-%m-%d")
        expenses.append({
            "date": expense_date, 
            "amount": float(amount), 
            "category": category, 
            "description": description
        })
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")

def filter_expenses_by_date(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return [exp for exp in expenses if start <= exp["date"] <= end]
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return []

def filter_expenses_by_category(category):
    return [exp for exp in expenses if exp["category"].lower() == category.lower()]

def show_summary():
    category_totals = {}
    total_expense = 0

    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
        total_expense += exp["amount"]

    print("\nExpense Summary:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    print(f"Total Expenses: ${total_expense:.2f}")

# **Updated Print Formatting**
def print_expenses(expense_list, title):
    print(f"\n{title}:")
    if not expense_list:
        print("No expenses found.")
        return
    print(f"{'Date':<12} {'Amount':<10} {'Category':<12} {'Description'}")
    print("-" * 50)
    for exp in expense_list:
        print(f"{exp['date'].strftime('%Y-%m-%d'):<12} ${exp['amount']:<10.2f} {exp['category']:<12} {exp['description']}")

# Example usage
add_expense("2023-10-10", 50.0, "Food", "Lunch at a restaurant")
add_expense("2023-10-15", 30.0, "Transport", "Bus fare")
add_expense("2023-10-20", 20.0, "Food", "Snacks")

print_expenses(filter_expenses_by_category("Food"), "Filtered by Category (Food)")
print_expenses(filter_expenses_by_date("2023-10-10", "2023-10-15"), "Filtered by Date (2023-10-10 to 2023-10-15)")
show_summary()

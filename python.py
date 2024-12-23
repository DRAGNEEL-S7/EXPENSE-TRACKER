# Define the expense tracker dictionary
expense_tracker = {}

def add_expense(date, category, amount, description):
    """Add an expense to the expense tracker."""
    if date not in expense_tracker:
        expense_tracker[date] = []
    expense_tracker[date].append
    ({'category': category,
        'amount': amount,
        'description': description})

def view_expenses():
    """Display all expenses."""
    for date, expenses in expense_tracker.items():
        print(f"Date: {date}")
        for expense in expenses:
            print(f"  Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        print()

def calculate_total_expense():
    """Calculate the total expense."""
    total = 0
    for expenses in expense_tracker.values():
        for expense in expenses:
            total += expense['amount']
    return total

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expense")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense = calculate_total_expense()
            print(f"Total Expense: {total_expense}")
        elif choice == '4':
            print("Exiting Expense Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

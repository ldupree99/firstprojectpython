# Creating a list that contains the different categories
categories = [
    "Fixed Expenses",
    "Variable Expenses",
    "Discretionary Expenses",
    # Add more categories/expenses as needed 
]

# Create an empty list that will store the expenses the user types
expenses = []

# Ask Username
user_name = input("Welcome! What's your name?: ")

# Introduction to app
print(f"Hi {user_name}! This is your personal Expense Tracker. We're here to help you take control of your finances and reach your goals. Let's get started on this journey together!")

# Loop through each category
for category in categories:
    add_expenses = input(f"Do you have entries for {category}? (yes/no): ").lower()

    # Check users response
    if add_expenses == 'yes':
        # Initialize a variable to control the loop
        add_another_expense = 'yes'

        # Use a while loop with the user's choice as the condition
        while add_another_expense.lower() == 'yes':
            expense = input(f"Enter your expense for {category}: ")
            expenses.append(expense)  # Add the expense to the list

            # Ask if the user wants to add another expense in the current category
            add_another_expense = input("Do you want to add another expense in this category? (yes/no): ")

        print(f"No more expenses added to {category} category")

        # Display expenses for the current category to the user

# Function to display expenses
def display_expenses(category, expense_list):
    print(f"\n{category} Expenses:")
    for expense in expense_list:
        print(f"- {expense}")

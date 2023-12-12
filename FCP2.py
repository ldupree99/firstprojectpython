<<<<<<< HEAD
# Function to add an expense to the tracker
def add_expense(expense_tracker, category, amount):
    """
    Add an expense to the expense tracker.

    Different Args added to function:
    - expense_tracker (dict): Dictionary to the store expenses.
    - category (str): Category of the expense.
    - amount (float)
    """
    # Check if the category exist in the expense tracker
    if category not in expense_tracker:
        #If not, create an empty list for that category
        expense_tracker[category] = []
    #Append the amount to the list of expenses for the specified category 
    expense_tracker[category].append(amount)

# Initialize an empty expense tracker
expense_tracker = {}

# Ask for user input
user_name = input("Welcome! What's your name?: ")

# Introduction to the app
print(f"Hi {user_name}! This is your personal Expense Tracker. Let's get started on this journey together!")

# Ask if there are expenses for Fixed Expenses category
add_fixed_expenses = input(f"Do you have entries for Fixed Expenses? (yes/no): ").lower()

# Check user's response
if add_fixed_expenses == 'yes':
    #initialize the promt for adding another expense
    add_another_expense = 'yes'

    #continue prompting the user as long as they want to add another expense
    while add_another_expense.lower() == 'yes':
        # Ask for expense details
        category = input("Enter the category for the expense: ")
        amount = float(input("Enter the amount of the expense: "))

        # Add the expense to the tracker
        add_expense(expense_tracker, category, amount)

        # Ask if the user wants to add another expense
        add_another_expense = input("Do you want to add another expense? (yes/no): ")


    # Print the expense tracker
    print("Expense Tracker:")
    for category, amounts in expense_tracker.items():
        #Display the total amount for each category
        print(f"{category}: {sum(amounts)}")

#Display a message when no more expenses are added
print("No more expenses added. Thank you for using the Expense Tracker!")
=======
# Function to add an expense to the tracker
def add_expense(expense_tracker, category, amount):
    if category != expense_tracker:
        expense_tracker[category] = []
    expense_tracker[category].append(amount)

# Initialize an empty expense tracker
expense_tracker = {}

# Ask for user input
user_name = input("Welcome! What's your name?: ")

# Introduction to the app
print(f"Hi {user_name}! This is your personal Expense Tracker. Let's get started on this journey together!")

# Ask if there are expenses for Fixed Expenses category
add_fixed_expenses = input(f"Do you have entries for Fixed Expenses? (yes/no): ").lower()

# Check user's response
if add_fixed_expenses == 'yes':
    add_another_expense = 'yes'

    while add_another_expense.lower() == 'yes':
        # Ask for expense details
        category = input("Enter the category for the expense: ")
        amount = float(input("Enter the amount of the expense: "))

        # Add the expense to the tracker
        add_expense(expense_tracker, category, amount)

        # Ask if the user wants to add another expense
        add_another_expense = input("Do you want to add another expense? (yes/no): ")

    # Print the expense tracker
    print("Expense Tracker:")
    for category, amounts in expense_tracker.items():
        print(f"{category}: {sum(amounts)}")

print("No more expenses added. Thank you for using the Expense Tracker!")
>>>>>>> 3541d227ced350c501b32bc5fac48c65fccb5cf0

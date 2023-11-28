#Extra flow chart python
categories = [ 
    "travel",
    "utilities",
    "food" 
]
user_choice = [
    "no",
    "yes"
]
userExpenses = []

moreExpenses = True 

for currentCategoryIndex in range( len( categories ) ):
    moreExpenses = True
    while moreExpenses:
        moreExpenses = float(input (f"Enter a {categories[currentCategoryIndex]} expense or press no to go to next category: " ) )
        userExpenses.append(f"You spent {moreExpenses} in {categories[currentCategoryIndex]}" )

        if moreExpenses == user_choice[0]:
            moreExpenses = False
            print("dwadad")
            break

for expense in userExpenses:
    print( expense ) 
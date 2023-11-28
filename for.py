#3rd main if 2nd flow chart python does not work
categories = [ 
    "travel",
    "utilities",
    "food" 
]

userExpenses = []

moreExpenses = True 

for currentCategoryIndex in range( len( categories ) ):
    moreExpenses = True
    while moreExpenses:
        moreExpenses = input(f"Enter a {categories[currentCategoryIndex]} expense or press no to go to next category: " )
        userExpenses.append(f"You spent {moreExpenses} in {categories[currentCategoryIndex]}" )

        if moreExpenses == "no":
            moreExpenses = False

for expense in userExpenses:
    print( expense ) 
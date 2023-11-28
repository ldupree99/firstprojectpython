#This is 2nd main
categories = [ 
    "travel",
    "utilities",
    "food" 
]

userExpenses = []
 
for currentCategoryIndex in range( len( categories ) ):
    moreExpenses = True
    while moreExpenses == True:
        user_input = (input(f"Enter a {categories[currentCategoryIndex]} expense or press no to go to next category: " ) )
        userExpenses.append(f"You spent {user_input} in {categories[currentCategoryIndex]}" )

        if user_input.lower() == "no":
            moreExpenses = False
            print("no gesgsgesfcd")
            break

for expense in userExpenses:
    print( expense ) 
import random                                                                                                                           # loads the random module which contains RNG related functions
'''
Name: Lucas Burt 
Date: 4/4/25
Bugs:
Bonuses: Calculates the total cost for all items, Ensures that the user is entering a valid number when asking for menu items.



'''

items = ["BigMac","Bacon Mcdouble","Fila-O-Fish","Mcchicken","Egg Mcmuffin","Cheese Burger","Mccrispy" ]                                # Lists the foods + creates a list (items)
prices = [6,3,5,3,3,2,4]                                                                                                                # Lists the cost per item + creates a list
sauces = ["Tangy BBQ","Sweet And Sour","Ketchup","Tarter Sauce","Creamy Ranch","Spicy Buffalo","Honey"]                                 # Lists the sauces per item + creates a list

while True:                                                                                                                             # creates forever loop 
    try:                                                                                                                                # initates a block of code where exeptions might occur 
        num_of_items = int(input('How many items? '))                                                                                   # set variable equal to the user's input of the question
    except ValueError:                                                                                                                  # states what exeptions to look for in the code (ex. "ValueError")
        print("Please select a number")                                                                                                 # tells the user to select a number of items
        continue
    
    total_price = 0                                                                                                                     # starting point for the sum of prices (sets the variable to 0)
    for i in range(num_of_items):                                                                                                       # use for loop to repeat for the number of items given by the user
        item = random.choice(items)                                                                                                     # get random item 
        sauce = random.choice(sauces)                                                                                                   # get random sauce 
        index = items.index(item)                                                                                                       # finds the index of item in items 
        price = prices[index]                                                                                                           # finds the price of item in items 
        print (f"{item} with {sauce} for ${price}")                                                                                     # tells the user their items, sauces, and prices
        total_price += price                                                                                                            # calculates the total price of items  
    print(f'Your total cost is ${total_price}')                                                                                         # tells the user their total price 

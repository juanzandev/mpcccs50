# Dictionary of food items and their prices, used as the menu for the program.
options = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Start defining the main function where the core logic of the program will reside.
def main():
    # Initialize a variable 'total' to keep a running total of the prices of the items ordered.
    
    # Convert the keys from the 'options' dictionary into a list so you can easily iterate through the food item names.
    
    # Create an infinite loop that will keep running until the user decides to stop the program.
    while True:
        # Inside the loop, do the following:
        # a. Prompt the user to enter the name of a food item. Be prepared to handle unexpected program exits.
        
        # b. Convert the user's input to lower case to ensure case-insensitive comparison with the menu items.
        
        # c. Iterate through the list of menu items. For each item, do the following:
            # i. Check if the user's input matches the current item in the list (considering case insensitivity).
            # ii. If it's a match, add the item's price to the total and print the current total formatted to two decimal places.
        
        # d. Handle any exceptions that might occur during the program's execution, like the user pressing Ctrl+C or Ctrl+D.
        
# Execute the program by calling the main function.
main()

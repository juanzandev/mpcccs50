'''
To use sys.argv in Python for handling command-line arguments, follow these quick steps:

Import sys: Include the sys module in your script to access sys.argv.
Access Arguments: Use sys.argv like a list. sys.argv[0] is the script name, and sys.argv[1], sys.argv[2], etc., are the command-line arguments passed to the script.
Check Arguments Length: Ensure you have the expected number of arguments using len(sys.argv) to prevent errors.
Example: Adding Two Numbers
This example demonstrates a script that accepts two numbers as command-line arguments and prints their sum.

----------python
import sys

def main():
    # Ensure exactly two arguments are provided
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])  # Convert first argument to float
            num2 = float(sys.argv[2])  # Convert second argument to float
            print(f"The sum of {num1} and {num2} is {num1 + num2}.")
        except ValueError:
            print("Please provide two numbers.")
    else:
        print("Usage: python script.py <number1> <number2>")

if __name__ == "__main__":
    main()
Running the Script
If your script is named add.py, run it from the command line like so:

------------bash
python add.py 5 7
This should output:

The sum of 5.0 and 7.0 is 12.0.
Key Points
Arguments are strings; convert them as needed (e.g., to int or float for numerical operations).
Always validate the number and type of arguments to avoid runtime errors.
--------------------------------------------------------------------------------------------------
Use the hints in the problem to learn how to use piglet

--------------------STEP BY STEP GUIDE----------------------------

# Import the PyFiglet module for creating ASCII art from text
# Import the sys module to access command-line arguments

# Define the main function of the script
    # Create a new Figlet object. More info in the hints
    # Retrieve a list of available fonts from the Figlet object. More info in the hints

    # Check if exactly two command-line arguments are provided (the script name and the -f option are not counted) Use if statement
        # If so, store the second argument as the font name.
    # Otherwise, print an error message and exit the program with a status code of 1. Use the sys library for this. Do not use exit()

    # Check if the provided font name is in the list of available fonts. Use for loop
        # If not, print an error message and exit the program with a status code of 1

    # Prompt the user for input text
    # Set the font of the Figlet object to the user-provided font name. More info in the hints

    # Print the input text rendered in the specified ASCII art font. More info in the hints

# Call the main function to execute the script

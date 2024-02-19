# Define the main function that contains the logic for collecting names and generating a farewell message.
def main():
    # Initialize an empty list to store the names entered by the user.

    # Initialize an empty string that will be used to build the output message.

    # Start an infinite loop to continuously prompt the user for names.
    while True:
        try:
            # Prompt the user for a name and store the input.

            # Append the inputted name to the list of names.
            
        except EOFError:  # This block executes when an EOF signal is detected (e.g., Ctrl+D/Z).
            # Calculate the number of names in the list.

            # Iterate over the list of names to construct the output string based on the number of names.
            for i in range(names):
                # If there is only one name, directly append it to the output string.
                # Print the farewell message with the single name and break out of the loop.

                # If there are exactly two names, construct the string using the first name, add " and ", then the last name.
                # Print the farewell message for two names and break out of the loop.

                # If there are more than two names, append each name followed by ", " to the output string until the penultimate name.

            # After the loop, if there are three or more names, add "and " and the last name to the output string.
            # This step ensures the correct grammar for lists of three or more items.

            # Print the final farewell message including all names correctly formatted.

            # Break the loop to end the program after printing the farewell message.

# Execute the main function to run the program.

'''LOGIC STATEMENT (MUST READ BEFORE YOU TACKLE THIS PROBLEM)
Infinite Loop for User Input: The program uses an infinite loop to continuously prompt the user for a date. This loop ensures that the program can repeatedly ask for input until a valid date is provided or the program is manually terminated.

Input Normalization: Upon receiving input, the program strips any leading or trailing whitespace, preparing the string for further processing. This step ensures that extra spaces do not affect the parsing of the date.

Format Detection and Parsing: The code checks the format of the user input by looking for specific characters ("/" for "MM/DD/YYYY" format, "," for "Month Day, Year" format). Based on the presence of these characters, it decides how to parse the input into its constituent parts (month, day, year).

Month Conversion: For inputs in the "Month Day, Year" format, the code converts the month from a word to a number by matching it against a predefined list of months. This step is crucial for standardizing the format.

Day and Month Validation and Formatting: The program ensures that both day and month numbers are two digits long, prepending a "0" if necessary. This standardization is part of the ISO 8601 requirement. It also checks that the month and day values are within valid ranges (1-12 for months, 1-31 for days), although it doesn't account for the varying lengths of different months or leap years.

Output Formatting: Once the date components are validated and standardized, the program outputs the date in the "YYYY-MM-DD" format. This format is chosen for its international recognition and ease of sorting, as it arranges date components from the largest to the smallest unit of time.

Error Handling: The program uses try-except blocks to handle errors gracefully. A ValueError might occur if the conversion of strings to integers fails (indicating invalid input), and the program simply continues to prompt for a new input. A KeyboardInterrupt (like pressing Ctrl+C) is caught to exit the program gracefully, providing a user-friendly way to stop execution.'''

#Step-by-step gude

# Define the main function for the program.
def main():
    # Define a list containing the names of all months in order.
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    # Specify the valid input formats and the desired output format as comments for clarity.

    # Start an infinite loop to continuously prompt the user for a date.
    while True:
        # Use a try-except block to handle errors and interruptions gracefully.

            # Prompt the user for a date, removing any leading or trailing whitespace.

            # Check if the date is in the mm/dd/yyyy format.

                # Split the date into month, day, and year.
                month, day, year = ?
                # Prepend a leading zero to the day if it is less than 10.
                  #USE THE VARIABLE SWAP TECHNIQUE (temp) TO HOLD A MEANINGFUL VALUE AND NOT LOSE IT BY CHANGING THE VALUE OF A MEANINGFUL VARIABLE.
                  # https://www.30secondsofcode.org/python/s/swap-      variables/#:~:text=The%20simplest%20way%20to%20swap,temp%20to%20the%20second%20variable.
                # Skip the rest of the loop if day does not satisfy the conditions.

                # Prepend a leading zero to the month if it is less than 10.

                # Validate the month and day are within the correct range, otherwise continue the loop.

                # Print the formatted date in yyyy-mm-dd format and break the loop if valid.

            # Check if the date is in the "month day, year" format.

                # Split the date into month, day, and year.

                # Convert the month name to a number by finding its index in the months list.

                # Remove the comma from the day and prepend a zero if it is less than 10.

                # Prepend a leading zero to the month if it is less than 10 after converting the month name to a number.

                # Validate the month and day are within the correct range, otherwise continue the loop.

                # Print the formatted date in yyyy-mm-dd format and break the loop if valid.

        # Handle ValueError to continue prompting the user for a valid date.

        # Handle KeyboardInterrupt to exit the program gracefully if the user attempts to stop the program.

# Call the main function to execute the program.
main()

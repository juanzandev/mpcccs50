# STEPS
# Define the main function.
    # Set the minimum and maximum percentage constants for fuel level indicators.

    # Start an infinite loop to continuously prompt for input until valid input is provided.
        # Prompt the user for the fuel percentage as a fraction (e.g., '1/4').
        # Use a try-except block to handle potential errors during input processing.
            # Split the input string into numerator and denominator based on the '/' character.
            # Convert the split strings into integers, catching ValueError for non-integer inputs.
            # Calculate the fuel percentage by dividing the numerator by the denominator.
            # Catch ZeroDivisionError to handle cases where the denominator is zero.

            # Check if the numerator is greater than the denominator. If so, prompt for input again.
            # Compare the calculated percentage to the predefined minimum and maximum thresholds.
                # If the percentage is below the minimum threshold, output 'E' for empty.
                # If the percentage is above the maximum threshold, output 'F' for full.
                # Otherwise, output the percentage as a whole number followed by a percentage sign.
            # If valid input is provided and processed, break out of the loop to end the program.

        # If an exception is caught, the loop continues, prompting for input again.

# Call the main function to execute the program.

# USEFUL FUNCTIONS

#map() Function:

#Applies a given function to each item of an iterable (like a list or tuple) and returns a map object.
#In the context of the problem, it can be used to convert the split numerator and denominator strings into integers simultaneously.
#Usage example: map(int, iterable)
#Reference: https://docs.python.org/3/library/functions.html#map

#round() Function:

#Rounds a number to a specified number of decimal places. By default, it rounds to the nearest whole number if no number of decimal places is specified.
#In the context of the problem, it can be used to round the calculated fuel percentage to the nearest whole number before displaying it.
#Usage example: round(number[, ndigits])
#Reference: https://docs.python.org/3/library/functions.html#round

#try-except Block:

#Used for handling exceptions (errors) that occur during code execution.
#Can be used to gracefully handle ValueError (invalid input format) and ZeroDivisionError (division by zero).
#Reference: https://docs.python.org/3/tutorial/errors.html

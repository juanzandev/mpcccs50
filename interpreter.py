#implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# explain the code
# 1. prompt the user for an arithmetic expression
# 2. use a string method to split the expression into three parts: x (first part), y (sum, subtraction, etc.), and z (second part)
# remember to check the reference for the correct string method to use: https://docs.python.org/3/library/stdtypes.html#string-methods
# remember to use the correct variable names for x, y, and z
# 3. convert x and z to floats
# 4. use an if-elif-else statement to determine which operation to perform
# print "Invalid input" if the user inputs an invalid operator
# remember that in python, the arithmetic expressions we simply use +, -, *, and / for addition, subtraction, multiplication, and division, respectively
# i.e 1 + 1, 1 - 1, 1 * 1, 1 / 1
# you may use a variable to store the result of the operation or you may simply print the result directly after each if-elif-else statement.
# 5. print the result
# 6. remember to initialize the main function at the end of the program

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 1. Initialize flags (booleans) to track the presence of specific characters and conditions.
    # 2. Check if the input's length is outside the acceptable range. If so, return False.
    # 3. Check if the first character of the input is not allowed. If so, return False.
    # 4. Loop through each character in the input: (Use range function to determine when to stop iterating)
    #    a. Mark the presence of certain types of characters.
    #    b. If an invalid character is encountered, return False.
    #    c. Handle specific character cases that affect the validity of the input.
    # 5. After the loop, perform final checks based on the characters found:
    #    a. Ensure the input ends with an acceptable character if certain characters were found.
    #    b. Ensure the correct order of character types in the input. (Numbers in between characters) Tip: you can go through a loop starting from the end.
    # 6. Return True if all conditions for a valid input are met.

main()

# LOGIC:
# Make sure you start from the least specific checks, such as the length of the input, and do the more specific ones at the end.

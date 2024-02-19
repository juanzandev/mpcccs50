# Import necessary libraries for system-level operations and making HTTP requests.
import sys
import requests

# Define the main function of the script.
def main():
    # Check if the correct number of command-line arguments has been provided.
    
    # Attempt to convert the second command-line argument to a float.
    try:
        # This variable will hold the number of Bitcoins the user wants to buy.
        
    # Handle the case where the conversion to float fails.
    except ValueError:
        # Exit the program with an error message if the argument is not a real number.
        
    # Attempt to make an HTTP request to the CoinDesk API.
    try:
        # Fetch the current price of Bitcoin in USD from the CoinDesk API.
        
        # If the HTTP request fails for any reason (4xx or 5xx responses), raise an HTTPError exception.
        
        # Parse the JSON response from the API and extract the current Bitcoin price in USD.
        
        # Calculate the total cost for the specified number of Bitcoins.
        
        # Print the total cost, formatted to four decimal places with a thousands separator.
        
    # Handle exceptions that may occur during the HTTP request.
    except requests.RequestException:
        # Exit the program with an error message if there's a problem with the network request.
        

# Check if the script is run directly (not imported) and call the main function.
if __name__ == "__main__":
    main()

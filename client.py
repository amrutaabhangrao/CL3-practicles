import xmlrpc.client

# Set up the client
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Prompt the user for an integer
try:
    number = input("Enter an integer to calculate its factorial: ")
    result = server.factorial(number)
    print(f"The factorial of {number} is {result}.")
except Exception as e:
    print(f"An error occurred: {e}")

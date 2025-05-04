import xmlrpc.server

def factorial(n):
    """Calculate the factorial of a number."""
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Set up the server
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")
server.register_function(factorial, "factorial")

# Run the server
server.serve_forever()

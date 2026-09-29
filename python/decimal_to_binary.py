# Declare a function named decimal_to_binary that takes one parameter: n
def decimal_to_binary(n):
    # Docstring - short description of what the function does
    """Convert a non-negative integer to its binary string representation."""
    # Special case: if the number is 0, return the string "0" directly
    if n == 0:
        # Return "0" and exit the function
        return "0"
    # Create an empty string to accumulate the binary digits
    binary = ""
    # Loop: keep dividing by 2 as long as n is greater than zero
    while n > 0:
        # Take the remainder of n divided by 2 (0 or 1 — the next bit)
        # and prepend it to the FRONT of the binary string
        binary = str(n % 2) + binary
        # Integer-divide n by 2 (drop the fractional part) to move to the next bit
        n //= 2
    # After the loop finishes, return the assembled binary string
    return binary


# Declare the main function — the entry point of the program
def main():
    # Read user input, convert the string to an integer
    number = int(input("Enter a decimal number: "))
    # Call the conversion function and store the result in a variable
    result = decimal_to_binary(number)
    # Print the result in the format: "Binary of <number> = <binary>"
    # The f-string inserts the values of number and result
    print(f"Binary of {number} = {result}")


# Check whether this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # If so, call main() to start the program
    main()
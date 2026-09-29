# Declare a function named binary_to_decimal that takes one parameter: binary_str
def binary_to_decimal(binary_str):
    # Docstring - short description of what the function does
    """Convert a binary string (e.g. '1101') to its decimal integer value."""
    # Initialize the accumulator that will hold the final decimal value
    decimal = 0
    # Get the length of the binary string (number of bits)
    length = len(binary_str)
    # Loop over each character in the binary string by index
    for i in range(length):
        # Extract the current character (bit) from the string
        bit = binary_str[i]
        # Convert the character '0' or '1' to the integer 0 or 1
        digit = int(bit)
        # Compute the power of 2 for this position:
        # leftmost bit has the highest power, rightmost has power 0
        power = length - 1 - i
        # Add the bit's contribution to the total decimal value
        decimal += digit * (2 ** power)
    # Return the final decimal number
    return decimal


# Declare the main function — the entry point of the program
def main():
    # Read user input as a string (no int() here because it's binary text)
    binary_str = input("Enter a binary number: ")
    # Call the conversion function and store the result in a variable
    result = binary_to_decimal(binary_str)
    # Print the result in the format: "Decimal of <binary> = <decimal>"
    # The f-string inserts the values of binary_str and result
    print(f"Decimal of {binary_str} = {result}")


# Check whether this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # If so, call main() to start the program
    main()
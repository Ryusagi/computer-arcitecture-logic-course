# Define a function called logical_or that takes two arguments: a and b
def logical_or(a, b):
    # Return 1 if either a or b is truthy (non-zero), otherwise return 0
    return 1 if (a or b) else 0


# Define the main function that will run the program
def main():
    # Print the title of the truth table
    print("Truth table for OR")
    # Print the column headers: A, B, and the result of A OR B
    print(" A | B | A OR B")
    # Print a separator line under the headers
    print("--+---+-----")

    # Outer loop: iterate a over the values 0 and 1
    for a in range(2):
        # Inner loop: iterate b over the values 0 and 1
        for b in range(2):
            # Print one row of the table:
            #   - value of a
            #   - value of b
            #   - result of logical_or(a, b)
            # f-string inserts the values into the formatted text
            print(f" {a} | {b} |   {logical_or(a, b)}")


# Check if this file is being run directly (not imported as a module)
if __name__ == "__main__":
    # If run directly, call the main function to start the program
    main()
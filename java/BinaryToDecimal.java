// Import the Scanner class to read user input
import java.util.Scanner;

// Declare a public class named BinaryToDecimal
public class BinaryToDecimal {

    // Declare a static method that takes a binary string and returns its decimal value
    public static int binaryToDecimal(String binaryStr) {
        // Initialize the accumulator that will hold the final decimal value
        int decimal = 0;

        // Get the length of the binary string (number of bits)
        int length = binaryStr.length();

        // Loop over each character in the binary string by index
        for (int i = 0; i < length; i++) {
            // Extract the current character (bit) from the string
            // charAt(i) returns a char, so we convert it to a String first
            char bitChar = binaryStr.charAt(i);

            // Convert the character '0' or '1' to the integer 0 or 1
            int digit = bitChar - '0';

            // Compute the power of 2 for this position:
            // leftmost bit has the highest power, rightmost has power 0
            int power = length - 1 - i;

            // Add the bit's contribution to the total decimal value
            // Math.pow returns a double, so we cast it to int
            decimal += digit * (int) Math.pow(2, power);
        }

        // Return the final decimal number
        return decimal;
    }

    // Main method — entry point of the program
    public static void main(String[] args) {
        // Create a Scanner to read input from the keyboard
        Scanner scanner = new Scanner(System.in);

        // Print a prompt asking the user to enter a binary number
        System.out.print("Enter a binary number: ");

        // Read the input as a String (no int conversion here)
        String binaryStr = scanner.nextLine();

        // Call the conversion method and store the result
        int result = binaryToDecimal(binaryStr);

        // Print the result in the format: "Decimal of <binary> = <decimal>"
        System.out.println("Decimal of " + binaryStr + " = " + result);

        // Close the scanner to release system resources
        scanner.close();
    }
}
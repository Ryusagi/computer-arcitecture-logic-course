// Import the Scanner class from java.util to read user input from the keyboard
import java.util.Scanner;

// Declare a public class named DecimalToBinary
public class DecimalToBinary {

    // Declare a static method named decimalToBinary that takes one int parameter: n
    // It returns a String (the binary representation)
    public static String decimalToBinary(int n) {
        // Special case: if the number is 0, return the string "0" directly
        if (n == 0) {
            // Return "0" and exit the method
            return "0";
        }

        // Create an empty String to accumulate the binary digits
        String binary = "";

        // Loop: keep dividing by 2 as long as n is greater than zero
        while (n > 0) {
            // Take the remainder of n divided by 2 (0 or 1 — the next bit)
            int remainder = n % 2;

            // Prepend the remainder to the FRONT of the binary string
            // (binary is built from the least significant bit upward)
            binary = remainder + binary;

            // Integer-divide n by 2 to move to the next bit
            n = n / 2;
        }

        // After the loop finishes, return the assembled binary string
        return binary;
    }

    // Declare the main method — the entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the standard input (keyboard)
        Scanner scanner = new Scanner(System.in);

        // Print a prompt asking the user to enter a decimal number
        System.out.print("Enter a decimal number: ");

        // Read the next integer the user types
        int number = scanner.nextInt();

        // Call the conversion method and store the result in a variable
        String result = decimalToBinary(number);

        // Print the result in the format: "Binary of <number> = <binary>"
        System.out.println("Binary of " + number + " = " + result);

        // Close the scanner to release system resources
        scanner.close();
    }
}
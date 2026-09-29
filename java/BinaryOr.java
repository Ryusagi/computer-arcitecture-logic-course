// Define a public class named LogicalOrTable
public class LogicalOrTable {

    // Define a static method called logicalOr that takes two int arguments: a and b
    public static int logicalOr(int a, int b) {
        // Return 1 if either a or b is non-zero (truthy), otherwise return 0
        return (a != 0 || b != 0) ? 1 : 0;
    }

    // Define the main method that will run the program
    public static void main(String[] args) {
        // Print the title of the truth table
        System.out.println("Truth table for OR");
        // Print the column headers: A, B, and the result of A OR B
        System.out.println(" A | B | A OR B");
        // Print a separator line under the headers
        System.out.println("--+---+-----");

        // Outer loop: iterate a over the values 0 and 1
        for (int a = 0; a < 2; a++) {
            // Inner loop: iterate b over the values 0 and 1
            for (int b = 0; b < 2; b++) {
                // Print one row of the table:
                //   - value of a
                //   - value of b
                //   - result of logicalOr(a, b)
                // printf inserts the values into the formatted text
                System.out.printf(" %d | %d |   %d%n", a, b, logicalOr(a, b));
            }
        }
    }
}
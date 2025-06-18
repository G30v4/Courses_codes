import java.util.Scanner;

public class TaskManagerEj1 {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        int totalPriority = 0;

        System.out.println("""
        ===* TASK MANAGER *===
        1. Add task
        2. View task
        3. Exit
        === ************** ===
        """);
        
        System.out.print("Select option: ");
        int option = sc.nextInt();
        sc.nextLine(); // to read new line when use: [nextInt() - nextDouble()]
        
        if (option >= 1 && option <= 3) {
            if (option == 1) {
                System.out.print("Input task name: ");
                String taskName = sc.nextLine();
                System.out.print("Priority (1-5): ");
                int priority = sc.nextInt();

                boolean isValid = priority >= 1 && priority <= 5;
                System.out.println("Is valid your priority? " + isValid);

                totalPriority += priority;

                System.out.println(String.format("""

                ===* NEW TASK ADDED *===
                Task added: %s
                Priority: %d
                ======================== 
                """, taskName, priority));
                System.out.println(String.format("Total Priority: %d", totalPriority));
            } else if (option == 2) {
                System.out.println("Working in this functionality!...");
            } else {
                System.out.println("See you then!!");
            }
        } else {
            System.out.println("Option not valid");
        }
        sc.close();
        
    }
}
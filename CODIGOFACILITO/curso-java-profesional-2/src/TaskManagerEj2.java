import java.util.Scanner;

public class TaskManagerEj2 {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        int option;
        int totalPriority = 0;

        do {
            System.out.println("""

            ===* TASK MANAGER *===
            1. Add task
            2. View task
            3. Exit
            === ************** ===
            """);
            
            System.out.print("Select option: ");
            option = sc.nextInt();
            sc.nextLine(); // to read new line when use: [nextInt() - nextDouble()]

            switch(option) {
                case 1 :
                    System.out.print("Input task name: ");
                    String taskName = sc.nextLine();
                    System.out.print("Priority (1-5): ");
                    int priority = sc.nextInt();

                    boolean isValid = priority >= 1 && priority <= 5;
                    System.out.println("Is valid your priority? " + isValid);

                    if (priority >= 1 && priority <= 5) {
                        totalPriority += priority;
                        System.out.println(String.format("""

                        ===* NEW TASK ADDED *===
                        Task added: %s
                        Priority: %d
                        ======================== 
                        """, taskName, priority));
                        System.out.println(String.format("Total Acummulative Priority: %d", totalPriority));
                    } else {
                        System.out.println("Priority not valid!");
                    }
                    break;
                case 2 :
                    System.out.println("Working in this functionality!...");
                    break;
                case 3 :
                    System.out.println("See you then!!");
                    break;
                default:
                    System.out.println("Option not valid");
            }
        } while (option != 3);
        sc.close();
    }
}
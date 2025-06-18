import java.util.Scanner;

public class TaskManagerEj3 {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        int option;
        int totalPriority = 0;

        do {
            showMenu();
            option = readOption(sc);
            totalPriority = executeOption(option, sc, totalPriority);            
        } while (option != 3);
        sc.close();
    }

    /**
     * Menú de opciones
     */
    public static void showMenu() {
        System.out.println("""
            ===* TASK MANAGER *===
            1. Add task
            2. View task
            3. Exit
            === ************** ===
            """);
    }

    /**
     * Solicitar opción del menú
     */
    public static int readOption( Scanner sc) {
        System.out.print("Select option: ");
        return sc.nextInt();
    }

    /**
     * Ejecuta tarea seleccionada
     */
    public static int executeOption(int option, Scanner sc, int totalPriority) {
        switch(option) {
            case 1 :
                totalPriority = addTask(sc, totalPriority);
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
        return totalPriority;
    }

    /**
     * Agrega nueva tarea
     */
    public static int addTask(Scanner sc, int totalPriority) {
        sc.nextLine(); // to read new line when use: [nextInt() - nextDouble()]
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

        return totalPriority;
    }
}
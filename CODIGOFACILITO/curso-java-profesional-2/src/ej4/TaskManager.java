import java.util.Scanner;

public class TaskManager {
    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        int option;
        int totalPriority = 0;
        Activity lastTask = null;

        do {
            showMenu();
            option = readOption(sc);
            Result result = executeOption(option, sc, totalPriority, lastTask);
            totalPriority = result.totalPriority;
            lastTask = result.task;
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
            2. View last task
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
    public static Result executeOption(int option, Scanner sc, int totalPriority, Activity task) {
        switch(option) {
            case 1 :
                return addTask(sc, totalPriority);
            case 2 :
                if (task != null) {
                    task.execute();
                } else {
                    System.out.println("There are not task registred yet!...");
                }
                
                break;
            case 3 :
                System.out.println("See you then!!");
                break;
            default:
                System.out.println("Option not valid");
        }
        return new Result(totalPriority, task);
    }

    /**
     * Agrega nueva tarea
     */
    public static Result addTask(Scanner sc, int totalPriority) {
        sc.nextLine(); // to read new line when use: [nextInt() - nextDouble()]
        System.out.print("Input task name: ");
        String taskName = sc.nextLine();
        System.out.print("Priority (1-5): ");
        int priority = sc.nextInt();

        if (priority >= 1 && priority <= 5) {
            totalPriority += priority;

            Task newTask = new Task(taskName, priority);
            System.out.println(String.format("""

            ===* NEW TASK ADDED *===
            Task added: %s
            Priority: %d
            ======================== 
            """, taskName, priority));
            System.out.println(String.format("Total Acummulative Priority: %d", totalPriority));
            return new Result(totalPriority, newTask);
        } else {
            System.out.println("Priority not valid!");
            return new Result(totalPriority, null);
        }
    }

    /**
     * Clase auxiliar para retornar multiples valores
     */
    public static class Result {
        int totalPriority;
        Activity task;

        public Result(int totalPriority, Activity task) {
            this.totalPriority = totalPriority;
            this.task = task;
        }
    }
}
import java.util.*;

public class TaskManagerAdvance {

    private static final Scanner sc = new Scanner(System.in);
    private static final ArrayList<Task> tasksList = new ArrayList<>();
    private static final HashMap<String, Task> tasksMap = new HashMap<>();
    private static int totalPriority = 0;

    public static void main(String[] arg) {
        int option;
        //Activity lastTask = null;

        do {
            showMenu();
            option = readOption(sc);
            executeOption(option);
            //totalPriority = result.totalPriority;
            //lastTask = result.task;
        } while (option != 6);
        sc.close();
    }

    /**
     * Menú de opciones
     */
    public static void showMenu() {
        System.out.println("""
            ===* TASK MANAGER *===
            1. Add task
            2. View tasks
            3. Search task by ID
            4. Delete task by ID
            5. View cumulative total of priorities 
            6. Exit
            === ************** ===
            """);
    }

    /**
     * Solicitar opción del menú
     */
    public static int readOption( Scanner sc) {
        System.out.print("Select option: ");
        return Integer.parseInt(sc.nextLine());
    }

    /**
     * Ejecuta tarea seleccionada
     */
    public static void executeOption(int option) {
        switch(option) {
            case 1 -> addTask();
            case 2 -> listTasks();
            case 3 -> searchTask();
            case 4 -> deleteTask();
            case 5 -> showAccumulator();
            case 6 -> System.out.println("See you then!!");
            default -> System.out.println("Option not valid");
        }
    }

    /**
     * Agrega nueva tarea
     */
    private static void addTask() {
        //sc.nextLine(); // to read new line when use: [nextInt() - nextDouble()]
        System.out.print("Input ID task: ");
        var id = sc.nextLine();

        if (tasksMap.containsKey(id)) {
            System.out.println("A task with this ID already exists");
            return;
        }
        System.out.print("Input task name: ");
        var taskName = sc.nextLine();
        System.out.print("Priority (1-5): ");
        var priority = Integer.parseInt(sc.nextLine()); //avoid problem of new line [nextInt() - nextDouble()]

        if (priority < 1 || priority > 5) {
            System.out.println("Priority not valid!");
            return;
        }
        

        var newTask = new Task(taskName, priority);
        tasksList.add(newTask);
        tasksMap.put(id, newTask);
        totalPriority += priority;

        System.out.println(String.format("""

        ===* NEW TASK ADDED *===
        Task added: %s
        Priority: %d
        ======================== 
        """, taskName, priority));
        System.out.println(String.format("Total Acummulative Priority: %d", totalPriority));        
    }

    /**
     * Listar tareas usando forEach()
     */
    private static void listTasks() {
        if (tasksMap.isEmpty()) {
            System.out.println("No exists tasks to show!");
            return;
        }
        System.out.println("===* LIST OF RECORDED TASKS *===");
        tasksMap.forEach((id, task) -> {
            System.out.println("Task ID: " + id + "-");
            task.execute(); // polimorfismo
        });
    }

    /**
     * Buscar tarea por ID
     */
    private static void searchTask() {
        System.out.print("Input ID task: ");
        var id = sc.nextLine();

        var t = tasksMap.get(id);
        if(t != null) {
            System.out.println("Task found: ");
            t.execute();
        } else {
            System.out.println("Ther is no task with that ID");
        }
    }

    /**
     * Eliminar tare por ID
     */
    private static void deleteTask() {
        System.out.print("Input ID task: ");
        var id = sc.nextLine();

        var t = tasksMap.remove(id);
        if (t != null) {
            tasksList.remove(t);
            totalPriority -= t.getPriority();
            System.out.println("Task successfully deleted!");
            showAccumulator();
        } else {
            System.out.println("Ther is no task with that ID");
        }
    }

    /**
     * Mostrar el acumulado de prioridades de Tareas
     */
    private static void showAccumulator() {
        System.out.println(String.format("Total Acummulative Priority: %d", totalPriority));
    }

}
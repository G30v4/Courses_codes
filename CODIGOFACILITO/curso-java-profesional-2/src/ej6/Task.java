public class Task extends Activity {
    private int priority;

    public Task(String name, int priority) {
        super(name);
        this.priority = priority;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    @Override
    public void execute() {
        System.out.println(String.format("""

            ===* TASK INFO *===
            Task added: %s
            Priority: %d
            ======================== 
            """, getName(), priority));
    }
}
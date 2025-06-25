public abstract class Activity {
    private String name;

    public Activity(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public abstract void execute();
}
import java.util.List;
import java.util.ArrayList;



public class Process {
    public String pid;
    public List<Resource> other_resources;
    public Process parent;
    public List<Process> children;
    public Status status;
    public int priority;
    public int reqNum;

    public Process(String id, int priority) {
        this.pid = id;
        this.priority = priority;
        this.status = new Status();
        this.status.type = "ready";
        this.status.list = "RL";
        this.children = new ArrayList<>();
        this.other_resources = new ArrayList<>();
        this.reqNum = 0;
    }
}

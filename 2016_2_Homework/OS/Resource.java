import java.util.ArrayList;
import java.util.List;

public class Resource {
    public String rid;
    public int total;
    public int remain;
    public List<Process> waiting_list;

    public Resource(String rid, int nums) {
        this.rid = rid;
        this.total = nums;
        this.remain = nums;
        waiting_list = new ArrayList<>();
    }
}

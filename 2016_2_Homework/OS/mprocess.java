import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class mprocess {

    private static Process runner = null;

    private static List<Process>[] RL = new List[3];
    private static List<Process> BL = new ArrayList<>();
    private static List<Resource> RS = new ArrayList<>();

    public static void insert(List<Process>[] lists, Process p) {
        lists[p.priority].add(p);
    }

    public static void create(String name, Integer priority)
    {
        System.out.println("create");
        Process p = new Process(name, priority);
        if(runner != null)
        {
            p.parent = runner;
            runner.children.add(p);
        }

        insert(RL, p);
        scheduler();
    }

    public static void help()
    {
        System.out.println("Help ....");
    }

    public static void init()
    {
        System.out.println("init--");
        String name = "init";
        create(name, 0);
        Process p = getProcessByName(name);
        scheduler();
        System.out.println("init done");
    }

    public static void delete(Process p)
    {
        System.out.println("delete");
        killTree(p);
        remove(RL, p);
        scheduler();
        System.out.println("delete done");
    }

    public static void killTree(Process p) {
        Process parentProcess = p.parent;
        for (Iterator i = p.children.iterator(); i.hasNext();) {
            Process child = (Process) i.next();
            //do-release-resource
            int l = child.other_resources.size() - 1;
            for(;l >= 0; l--)  {
                Resource r = child.other_resources.get(l);
                release(r, 1);
                remove(child.other_resources, r, 1);
            }
            killTree(child);
            p.children.remove(child);
        }
        int l = p.other_resources.size() - 1;
        for(;l >= 0; l--)  {
            Resource r = p.other_resources.get(l);
            release(r, 1);
            remove(p.other_resources, r, 1);
        }
        parentProcess.children.remove(p);
    }

    public static void scheduler() {
        //find highest priority process
        Process toStart = null;
        for (int i = 2; i >= 0; i--) {
            if (RL[i].isEmpty()) continue;
            else {
                toStart = RL[i].get(0);
                break;
            }
        }
        if (runner == null || runner.priority < toStart.priority || runner.status.type != "running") {
            preempt(toStart);
        }
        System.out.printf("Now process %s is running.\n", runner.pid);
    }

    public static void preempt(Process p) {
        runner = p;
        runner.status.type = "running";
    }

    public static void timeout() {
        remove(RL, runner);
        runner.status.type = "ready";
        insert(RL, runner);
        scheduler();
    }

    public static void remove(List<Process>[] lists, Process p) {
        lists[p.priority].remove(p);
    }

    public static void remove(List<Resource> rs, Resource r, int n) {
        for (int i = 0; i < n; i++) rs.remove(r);
    }

    public static Process getProcessByName(String name)
    {
        for (List<Process> l : RL)
        {
            for (Process p : l)
            {
                if(p.pid.equals(name))
                {
                    return p;
                }
            }
        }
        for (Process p : BL)
        {
            if(p.pid.equals(name))
            {
                return p;
            }
        }

        return null;
    }

    public static Resource getResourceByName(String name)
    {
        for (Resource r : RS)
        {
            if(r.rid.equals(name))
            {
                return r;
            }
        }

        return null;
    }
    public static void request(Resource r, int n)
    {
        runner.reqNum = n;
        if (r.remain >= n)
        {
            r.remain -= n;
            for(int i = 0; i < n; i++)
            {
                runner.other_resources.add(r);
            }
        }
        else
        {
            if (n > r.total)
            {
                System.out.println("Not so much resource, give me money to update my hardware.");
                return;
            }
            runner.status.type = "blocked";
            runner.status.list = "BL";
            remove(RL, runner);
            BL.add(runner);
            r.waiting_list.add(runner);
        }
        scheduler();
    }


    public static void release(Resource r, int n)
    {
        remove(runner.other_resources, r, n);
        r.remain += n;
        int l = r.waiting_list.size() - 1;
        for(; l >= 0 && r.remain >= runner.reqNum; l--)
        // while(r.waiting_list != null && r.remain >= runner.reqNum)
        {
            Process p = r.waiting_list.get(l);
            r.remain -= runner.reqNum;
            r.waiting_list.remove(p);
            BL.remove(p);
            p.status.type = "ready";
            p.status.list = "RL";
            insert(RL, p);
            p.other_resources.add(r);

        }
        scheduler();
    }

    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            RL[i] = new ArrayList<>();
        }
        Resource R1 = new Resource("R1", 1); RS.add(R1);
        Resource R2 = new Resource("R2", 2); RS.add(R2);
        Resource R3 = new Resource("R3", 3); RS.add(R3);
        Resource R4 = new Resource("R4", 4); RS.add(R4);

        Scanner in = new Scanner(System.in);
        String line = "line";

        while(line != "")
        {
            line = in.nextLine();
            args = line.split(" ");
            switch(args[0])
            {
                case "q":
                case "quit":
                case "exit":
                {
                    System.out.println("-----exit------");
                    System.exit(0);
                    break;
                }
                case "init":
                {
                    init();
                    break;
                }
                case "cr":
                {
                    create(args[1], Integer.parseInt(args[2]));
                    break;
                }
                case "de":
                {

                    Process p = getProcessByName(args[1]);
                    System.out.println(p);
                    if (p != null)
                    {
                        delete(p);
                    }
                    break;
                }
                case "req":
                {
                    Resource r = getResourceByName(args[1]);
                    if (r != null)
                    {
                        request(r, Integer.parseInt(args[2]));
                    }

                    break;
                }
                case "rel":
                {
                    Resource r = null;
                    r = getResourceByName(args[1]);
                    if (r != null)
                    {
                        release(r, Integer.parseInt(args[2]));
                    }
                    break;
                }
                case "to":
                {
                    timeout();
                    break;
                }
                default:
                {
                    help();
                }
            }
        }
    }
}

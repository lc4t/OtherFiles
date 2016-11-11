import java.util.Scanner;


public class loop
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] textArray = {"学长我零基础咋办? 看书啊。", "学长我没电脑咋办? 买啊。", "学长我没时间咋办? 别水群撒。"};
        for (int i = 0; i < n; i++)
        {
            System.out.println(textArray[i % 3]);
        }
    }
}

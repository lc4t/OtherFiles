import java.util.Scanner;

public class t_o
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] nums = input.split(" ");
        double sum = 0;
        int length = nums.length;
        for (int i = 0; i < length; i++)
        {
            sum += Double.parseDouble(nums[i]);
        }
        System.out.println(sum/length);

    }
}

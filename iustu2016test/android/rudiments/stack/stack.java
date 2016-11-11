import java.util.Stack;
import java.util.Scanner;

public class stack
{
    public static void main (String[] args)
    {
        Stack<Integer> st = new Stack<Integer>();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] nums = input.split(" ");
        int length = nums.length;
        int index = 0, deep = 0;
        for (int i = 0; i < length;)
        {
            if (st.empty() || st.peek() < Integer.parseInt(nums[i]))
            {
                st.push(index);
                deep = (st.size() > deep) ? st.size() : deep;
                index++;
            }
            else
            {
                st.pop();
                i++;
            }
        }

        if (st.empty() == true)
        {
            System.out.println(String.format("true %d", deep));
        }
        else
        {
            System.out.println("false");
        }
    }
}

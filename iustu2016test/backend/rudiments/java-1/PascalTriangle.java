import java.util.Scanner;
import java.util.InputMismatchException;

public class PascalTriangle
{
    public static void main (String[] args)
    {
        final int START_NUM = 2;
        final int START_NO = 1;

        long num = 1;
        Scanner sc = new Scanner(System.in);
        try
        {
            int endFloor = sc.nextInt();
            if (endFloor > 62 || endFloor <= 0)
            {
                System.out.println("Input was not support");
            }
            else
            {
                System.out.println("1");
                for (int floor = START_NUM; floor <= endFloor; num = START_NO, floor++)
                {
                    System.out.print("1 ");
                    for (int no = START_NO; no <= floor - 2; no++)
                    {
                        num = (floor - no) * num / no;
                        System.out.print(String.format("%d ", num));
                    }
                    System.out.println("1");
                }
            }

        }
        catch (InputMismatchException e)
        {
            System.out.println("Input error, may not int");
        }
        catch (Exception e)
        {
            System.out.println("Wrong:" + e);
        }
    }
}

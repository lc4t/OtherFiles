import java.util.Scanner;

public class logic
{
    public static void main (String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        if (n < 1 || m < 1)
        {
            System.out.println("false");
        }
        else
        {
            if (n < m)
            {
                n = m - n;
                m = m - n;
                n = m + n;
            }
            //assert n >= m

            if (n == m )
            {
                if (n <= 29)
                {
                    System.out.println("true false");
                }
                else
                {
                    System.out.println("false");
                }
            }
            else if (n > 30)
            {
                System.out.println("false");
            }
            else
            {
                if (n < 21 && m <= 19)
                {
                    System.out.println("true false");
                }
                else if (n >= 21 && n <= 29 && m == n - 1)
                {
                    System.out.println("true false");
                }
                else if (n == 21 && m <= 19)
                {
                    System.out.println("true true");
                }
                else if (n >= 22 && n <= 30 && m == n - 2)
                {
                    System.out.println("true true");
                }
                else if (n == 30 && m == 29)
                {
                    System.out.println("true true");
                }
                else
                {
                    System.out.println("false");
                }
            }

        }

    }
}

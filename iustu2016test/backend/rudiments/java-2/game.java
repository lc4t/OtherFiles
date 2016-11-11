import java.util.Scanner;

public class game
{
    public static void main (String[] args)
    {

        try
        {
            Person player1 = new Person();
            Person player2 = new Person();

            while(player1.HP > 0)
            {
                player2 = player1.attack(player2);
                if (player2.HP > 0)
                {
                    player1 = player2.attack(player1);
                }
                else
                {
                    break;
                }
            }
        }
        catch (Exception e)
        {
            System.out.println("Wrong:" + e);
        }
    }
}



class Person implements Iprint
{
    public String name;
    public int HP;
    public int ATN;

    public Person()
    {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] inputArgs = input.split("一个人叫|,HP 为 |,攻击力为 ");
        this.name = inputArgs[1];
        this.HP = Integer.parseInt(inputArgs[2]);
        this.ATN = Integer.parseInt(inputArgs[3]);
    }

    public Person(String name, int HP, int ATN)
    {
        this.name = name;
        this.HP = HP;
        this.ATN = ATN;
    }

    public Person attack(Person victim)
    {
        victim.HP -= this.ATN;

        if (victim.HP <= 0)
        {
            printAttack(this.name, victim.name, this.ATN, 0);
            printWin(this.name);
        }
        else
        {
            printAttack(this.name, victim.name, this.ATN, victim.HP);
        }
        return victim;
    }

    public void printAttack(String injurerName, String victimName, int ATN, int HP)
    {
        System.out.println(String.format("%s 攻击了%s,%2$s 受到了 %d 点伤害,剩余生命 %d ", injurerName, victimName, ATN, HP));
    }

    public void printWin(String name)
    {
        System.out.println(String.format("%s赢了", name));
    }
}

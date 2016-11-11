#include "Stack.h"



// 48-57


bool Is_Operator(char in)
{
    switch(in)
    {
        case '+':
        case '-':
        case '*':
        case '/':
        case '(':
        case ')':
            return true;
            // break
        default:
            return false;
    }
}




int Operator_Level(char o)
{
    if (o == '+' || o == '-')
    {
      return 0x1;
    }
    else if (o == '*' || o == '/')
    {
      return 0x10;
    }
    else
    {
      return -1;
    }
}


// void printo(Linklist stack, char* s)
// {
//   Linknode p = stack.next;
//   printf("--------------->>");
//   printf("%s\n", s);
//   while(p != NULL)
//   {
//       printf("%c", p->data);
//       p = p->next;
//   }
//   printf("\n---------------00\n");
// }
//
// void printn(Linklist stack, char* s)
// {
//   Linknode p = stack.next;
//   printf("--------------->>");
//   printf("%s\n", s);
//   while(p != NULL)
//   {
//       printf("%d", p->data);
//       p = p->next;
//   }
//   printf("\n---------------00\n");
// }


void Calc(Linklist* operator, Linklist* numbers)
{
  int num1 = Pop_Stack(numbers);
  int num2 = Pop_Stack(numbers);

  switch(Pop_Stack(operator))
  {
  case '+':
      Push_Stack(numbers, num2 + num1);
      break;
  case '-':
      Push_Stack(numbers, num2 - num1);
      break;
  case '*':
      Push_Stack(numbers, num2 * num1);
      break;
  case '/':
      Push_Stack(numbers, num2 / num1);
      break;
  default:
      printf("error\n");

  }
}

int main(int argc, const char* argv[])
{

    Linklist operator;
    Init_Stack(&operator);
    Push_Stack(&operator, '#'); // avoid for empty stack..

    Linklist numbers;
    Init_Stack(&numbers);

    char in = 0;
    while(scanf("%c", &in) && in != '\n' && in != '\r')
    {
        // printf("in:%c\n", in);
        if (in == ' ')
        {
            continue;
        }
        if (Is_Operator(in))
        {
            if (in == '+' || in == '-' || in == '*' || in == '/')
            {
                if (Operator_Level(Top_Stack(operator)) < Operator_Level(in))    // lower than in
                {
                    // printf("compare: %c < %c success, push\n", Top_Stack(operator), in);
                    Push_Stack(&operator, in);
                }
                else
                {
                    // printf("compare: %c >= %c success, calc\n", Top_Stack(operator), in);
                    Calc(&operator, &numbers);
                    Push_Stack(&operator, in);
                }
            }
            else if (in == '(')
            {
                Push_Stack(&operator, in);
            }
            else if (in == ')')
            {
                while (Top_Stack(operator) != '(')
                {
                    Calc(&operator, &numbers);
                }
                Pop_Stack(&operator);
            }
            else
            {
              printf("nothing:%c\n", in);
            }
        }
        else
        {
            Push_Stack(&numbers, in - '0');
        }
    }
    while(Top_Stack(operator) != '#')
    {
      Calc(&operator, &numbers);
    }
    printf("%d\n", Pop_Stack(&numbers));



    return 0;
}

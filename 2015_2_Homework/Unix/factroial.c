#include <stdio.h>

int main(int argc, const char* argv[])
{
    int num = 0;
    long long sum = 1;
    printf("Input a integer between [0, 21):");
    scanf("%d", &num);
    if (num < 0 || num > 20)
    {
        printf("Do you want to pwn me?\nBye bye~\n");
    }
    else
    {
        for (; num > 0; num--)
        {
            sum *= num;
        }
        printf("You get %lld\n", sum);
    }
    return 0;
}

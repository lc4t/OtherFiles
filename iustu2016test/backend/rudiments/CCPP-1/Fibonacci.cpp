#include <iostream>

#define N 20

int Fibonacci(int* f, int n)
{
    if (f[n] != 0)
    {
        // will not step into else..if
    }
    else if (n == 1 || n == 2)
    {
        f[n] = 1;
    }
    else
    {
        f[n] = Fibonacci(f, n - 1) + Fibonacci(f, n - 2);
    }
    return f[n];
}


int main(int argc, const char* argv[])
{
    int f[N + 1] = {0}; // [wiki]By definition, the first two numbers in the Fibonacci sequence are either 1 and 1, or 0 and 1
    Fibonacci(f, 20);
    for(int i = 1; i <= N; i++)
    {
        std::cout << f[i] << std::endl;
    }
    return 0;
}

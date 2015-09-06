#include <iostream>
#include <cstdarg>
using namespace std;

int max(int a, int b,...)
{
    va_list ptr;
    int  number;
    va_start(ptr,b);
    number = va_arg(ptr, int);
    cout<<number<<endl;
    for (int i = 1;number != -1;i++)
    {
        number = va_arg(ptr, int);
        cout<<number<<endl;
    }
    return 1;
}
int main()
{

    max(1,2,3,4,5,6,7,8,9,-1);
}
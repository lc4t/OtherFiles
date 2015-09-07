#include <iostream>
#include <cstdarg>
#include <map>
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

    map<string, string> phone2name;
    phone2name.insert(map<string, string>::value_type("186837","wang"));

    auto search = phone2name.find("186837");
    cout<<search<<endl;
}
#include <stdio.h>
static char buff[256];
static char *string;
int main()
{
        printf("please input a string:\n");
        gets(string);
        printf("your string is: %s\n", string);
}

#include <stdio.h>

void bubbleSort(int length, int* array)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = i; j < length; j++)
        {
            if (array[i] > array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

int main(int argc, const char* argv[])
{
    int array[10] = {4,6,1,3,8,3,1,3,6,1};
    bubbleSort(10, array);
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", array[i]);
    }
}

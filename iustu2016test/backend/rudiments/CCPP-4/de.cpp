#include <iostream>
#include <algorithm>

#define N 10

void bubbleSort(int length, int* array)
{
    for (int i = 0; i < length; i++)
    {
        for (int j = i; j < length; j++)
        {
            if (array[i] < array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

// use STL first
bool cmp(const int n, const int m)
{
    return n > m;
}

int main(int argc, const char* argv[])
{
    int num[N] = {10,3,20,55,7,35,91,75,84,95};
    std::sort(num, num + N, cmp);
    // bubbleSort(10, num);
    for (int i = 0; i < N; i++)
    {
        std::cout << num[i] << std::endl;
    }
    return 0;
}

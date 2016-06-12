#include <algorithm>
#include <deque>
#include <iostream>
#include <numeric>

void popFrontTimes(std::deque<int>& d, int times)
{
    for (;times > 0; times--)
    {
        d.pop_front();
    }
}

void print(const std::deque<int>& d)
{
    for (int n : d)
    {
        std::cout << n << " ";
    }
    std::cout << std::endl;
}

bool ifLargeThan11(const int &a)
{
    return a > 11;
}

int main(int argc, const char* argv[])
{

    std::deque<int> num = {11, 12, 13, 2, 3, 4, 5, 6, 7, 16, 17, 18};

    sort(num.begin(), num.end());
    popFrontTimes(num, 3);

    std::cout << "sum:" << std::accumulate(num.begin(), num.end(), 0) << std::endl;

    num.erase(std::remove_if(num.begin(), num.end(), ifLargeThan11), num.end());
    print(num);

    return 0;
}

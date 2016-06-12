#include <algorithm>
#include <functional>
#include <iostream>
#include <iterator>
#include <list>
#include <vector>

void printOddEvenNumbers(const std::vector<int>& num)
{
    std::vector<int> evenNum;
    std::vector<int> oddNum;

    std::modulus<int> mod;
    std::ostream_iterator<int> evenOS(std::cout, " is even\n");
    std::ostream_iterator<int> oddOS(std::cout, " is odd\n");

    for (auto i : num)
    {
        if(mod(i, 2) == 0)
        {
            evenNum.push_back(i);
        }
        else
        {
            oddNum.push_back(i);
        }
    }
    copy(evenNum.begin(), evenNum.end(), evenOS);
    copy(oddNum.begin(), oddNum.end(), oddOS);
}

std::list<int> splitToList(const std::vector<int>& num, int left, int right)
{
    std::list<int> answerNum;

    for (auto i: num)
    {
        if (i >= left && i < right)
        {
            answerNum.push_back(i);
        }
    }

    return answerNum;
}

void printList(std::list<int> num)
{
    for (auto i : num)
    {
        std::cout << i << " " ;
    }
}

int main(int argc, const char* argv[])
{
    std::vector<int> num = {11, 12, 13, 2, 3, 4, 5, 6, 7, 16, 17, 18};

    printOddEvenNumbers(num);
    printList(splitToList(num, 7, 17));

    return 0;
}

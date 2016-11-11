#include <iostream>


int FebDays(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ? 29 : 28;
}

int MonthsDelay(int month, int year)
{
    int delay = 0;
    switch(month)
    {
        case 12:
            delay += 30;
        case 11:
            delay += 31;
        case 10:
            delay += 30;
        case 9:
            delay += 31;
        case 8:
            delay += 31;
        case 7:
            delay += 30;
        case 6:
            delay += 31;
        case 5:
            delay += 30;
        case 4:
            delay += 31;
        case 3:
            delay += FebDays(year);
        case 2:
            delay += 31;
        case 1:
            return delay;
        default:
            // error
            return -1;
    }
}

int main(int argc, const char* argv[])
{
    int year = -1, month = -1, day = -1;
    std::cin >> year >> month >> day;
    if (year > 0 && month > 0 && month < 13 && day > 0 && day <= 31)
    {
        if (month == 2 && day > FebDays(year))
        {
            //
        }
        else
        {
            std::cout << MonthsDelay(month, year) + day << std::endl;
        }
    }


    return 0;
}

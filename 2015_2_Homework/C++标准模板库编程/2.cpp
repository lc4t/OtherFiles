#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

#define GRADE_LENGTH 4
#define GRADE_START 2010
#define GRADE_COUNT 3

void printGradeCount(const std::map<std::string, std::string>& student)
{
    int* count = new int[GRADE_COUNT]();
    for (std::pair<std::string, std::string> it : student)
    {
        int number;
        std::stringstream ss;
        ss << it.second.substr(0, GRADE_LENGTH);
        ss >> number;
        count[number - GRADE_START] ++;
    }
    for (int i = 0; i < GRADE_COUNT; i++)
    {
        std::cout << i + GRADE_START << " grade sum:" << count[i] << std::endl;
    }
    free(count);
}

void printQueryAnswerByName(const std::map<std::string, std::string>& student, const std::string& queryString)
{
    auto search = student.find(queryString);
    if (search != student.end())
    {
        std::cout << "Found:" << search->first << " " << search->second << '\n';
    }
    else
    {
        std::cout << "Not found\n";
    }
}

void printQueryAnswerByCode(const std::map<std::string, std::string>& student, const std::string& queryString)
{
    for (std::pair<std::string, std::string> it : student)
    {
        if (it.second == queryString)
        {
            std::cout << "Found:" << it.first << " " << it.second << '\n';
            return;
        }
    }

    std::cout << "Not found\n";
}

int main(int argc, const char* argv[])
{
    std::map<std::string, std::string> student = {
                                                    {"张三", "2011123"},
                                                    {"王二", "2011235"},
                                                    {"刘七", "2012009"},
                                                    {"唐六", "2012676"},
                                                    {"堂八", "2010527"}
                                                    };

    printGradeCount(student);


    std::string queryType, queryString;
    while (queryType != "q" && queryType != "exit")
    {
        std::cout << "input query type[name/code], q/exit:";
        std::cin >> queryType;
        if (queryType == "name")
        {
            std::cout << "input name:";
            std::cin >> queryString;
            printQueryAnswerByName(student, queryString);
        }
        else if (queryType == "code")
        {
            std::cout << "input student code:";
            std::cin >> queryString;
            printQueryAnswerByCode(student, queryString);
        }
        else if (queryType != "q" && queryType != "exit")
        {
            std::cout << "input error" << std::endl;
        }
        else
        {
            //
        }
    }


    return 0;
}


#include "include/PhoneBook.h"
#include <iterator>
using namespace std;
int main(int argc, char *argv[])
{
	PhoneBook phonebook;
	phonebook.AddStudent("wang","he","183");
	struct stu student = phonebook.Search("w");
	std::cout<<student.name<<std::endl;
	std::cout<<student.address<<std::endl;
	for (set<string>::iterator i = student.phoneNumber.begin(); i != student.phoneNumber.end(); i++)
	{
		std::cout<<(*i)<<std::endl;
	}


}

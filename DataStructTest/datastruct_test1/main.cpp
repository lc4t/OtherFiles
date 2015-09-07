
#include "include/PhoneBook.h"

using namespace std;
int main(int argc, char *argv[])
{
	PhoneBook phonebook;
	phonebook.AddStudent("wang","he","183");
	phonebook.PrintInfoByName("wang");
	phonebook.AddStudent("wang","1","123");
	phonebook.PrintInfoByName("wang");
//	struct stu student = phonebook.GetInfoByName("wang");
//	std::cout<<student.name<<std::endl;
//	std::cout<<student.address<<std::endl;
//	for (vector<string>::iterator i = student.phoneNumber.begin(); i != student.phoneNumber.end(); i++)
//	{
//		std::cout<<(*i)<<std::endl;
//	}



// TESTING CODE
//	std::map<string,string> example = {{"123","1"},{"321","2"},{"a","3"},{"01","0"}};
//
//	example.insert(map<string, string>::value_type("2","wang"));
//	auto search = example.find("2");
//	if(search != example.end())
//	{
//		std::cout << "Found " << search->first << " " << search->second << '\n';
//	}
//	else
//	{
//		std::cout << "Not found\n";
//	}
//
//	example["123"] = "219030";
//	for (auto it = example.cbegin(); it != example.cend(); ++it)
//	{
//	    std::cout << it->first << " : " << it->second << '\n';
//	}
// END TESTING

}

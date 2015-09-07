/*
 * PhoneBook.cpp
 *
 *  Created on: 2015年9月7日
 *      Author: lc4t
 */

#include "PhoneBook.h"


PhoneBook::PhoneBook()
{
	std::cout<<"Your create a phonebook."<<std::endl;
	noneStudent.address = "";
	noneStudent.name = "";

//	for(;;)
//	{
//
//	}

}


int PhoneBook::Count()
{
	return students.size();
}


void PhoneBook::AddStudent(std::string name, std::string address, std::string phoneNumber)
{
	if (CheckNameExist(name))
	{
		std::cout<<"The name is exist,what do you want to do with it?"<<std::endl;
		std::cout<<"1) Delete it"<<std::endl;
		std::cout<<"2) Edit it"<<std::endl;
		std::cout<<"3) Add the new phone number you input"<<std::endl;
		std::cout<<"Input the number:";
		int mode = -1;
		std::cin>>mode;

		switch(mode)
		{
		 case 1:
			 DeleteStudent(name);
			 break;
		 case 2:
			 EditMode(name);
			 break;
		 case 3:
			 AddPhoneNumberByName(name, phoneNumber);
		}
			// add phoneNumber
	}
	else	// new name
	{
		struct stu newStudent;
		newStudent.name = name;
		newStudent.address = address;
		newStudent.phoneNumber.push_back(phoneNumber);

		students.insert(std::map<std::string, struct stu>::value_type(name, newStudent));//add student info
		phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name)); 	//add phone2name
	}


}


void PhoneBook::AddPhone2Name(std::string phoneNumber, std::string name)
{
	// who use it should KEEP the phoneNumber not in phoneList
	// should have check for the phoneNumber not in phoneList
	phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name));

}


//void PhoneBook::AddPhone2List(std::string phoneNumber)
//{
//
//}

std::string PhoneBook::GetNameByPhoneNumber(std::string phoneNumber)
{
	auto search = phone2name.find(phoneNumber);
	if(search != phone2name.end())
	{
//		std::cout << "Found " << search->first << " " << search->second << '\n';
		return search->second;
	}
	else
	{
		return  NOT_FOUND;
	}
}


void PhoneBook::PrintInfoByName(std::string name)
{
	struct stu student = GetInfoByName(name);

	std::cout<<"<-*******Current Student Info*******->"<<std::endl;
	std::cout<<"name: "<<student.name<<std::endl;
	std::cout<<"address:"<<student.address<<std::endl;
	std::cout<<"phone(s): ";
	for (auto it : student.phoneNumber)
		{
			std::cout<<it<<",";
		}
	std::cout<<std::endl<<"<-*******End Student Info*******->"<<std::endl;


}


void PhoneBook::EditMode(std::string name)
{
	std::cout<<"<-*******You are in EDIT MODE*******->"<<std::endl;
	PrintInfoByName(name);
	int code = -1;
	std::cout<<"1) change name"<<std::endl;
	std::cout<<"2) change address"<<std::endl;
	std::cout<<"3) change phone numbers"<<std::endl;
	std::cout<<"4) delete a phone number"<<std::endl;
	std::cout<<"Input the number:";
	std::cin>>code;
	std::string newData = "";
	switch(code)
	{

		case 1:
			std::cout<<"Input a new name: "<<std::endl;
			std::cin>>newData;
			AddStudent(newData, students[name].address, students[name].phoneNumber);
			DeleteStudent(name);
			return ;
		case 2:
			std::cout<<"Input a new address: "<<std::endl;
			std::cin>>newData;
			ChangeAddress(name, newData);
			break;
		case 3:
			int count = GetCountOfPhoneNumbers(name);
			std::cout<<"There are(is) "<<count<<" phone number(s)."<<std::endl;
			for (int i = 0; i< count; i++)
			{
				std::cout<<i + 1<<") "<<students[name].phoneNumber[i]<<std::endl;
			}
			std::cout<<"Input the number of phone to change: ";
			int code = -1;
			std::cin>>code;
			code --;
			std::cout<<"Input the new phone number: ";
			std::cin>>newData;
			ChangePhoneNumbers(name, code, newData);
			break;

	}
}


void PhoneBook::DeleteStudent(std::string name)
{
		//delete list of phone
		int count = GetCountOfPhoneNumbers(name);
		for (int i = 0; i < count; i++)
		{
			phone2name.erase(students[name].phoneNumber[i]);
		}
		students.erase(name);

}

int PhoneBook::GetCountOfPhoneNumbers(std::string name)
{
	return students[name].phoneNumber.size();
}

void PhoneBook::ChangePhoneNumbers(std::string name, int index, std::string phoneNumber)
{

	phone2name.erase(students[name].phoneNumber[index]);
	students[name].phoneNumber[index] = phoneNumber;
	phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name));

}

void PhoneBook::ChangeAddress(std::string name, std::string address)
{
	students[name].address = address;
}


struct stu PhoneBook::GetInfoByName(std::string name)
{
	auto search = students.find(name);
	if(search != students.end())
	{
		return search->second;
	}
	else
	{
		return  noneStudent;	//NOT FOUND
	}

}



struct stu PhoneBook::GetInfoByPhoneNumber(std::string phoneNumber)
{
	return GetInfoByName((GetNameByPhoneNumber(phoneNumber)));
}
//void PhoneBook::AddStudent2(std::string name, std::string address, ...)
//{
//	std::cout<<123;
//	struct stu newStudent;
//	newStudent.name = name;
//	newStudent.address = address;
//	std::cout<<address;
//	va_list ptr;
//	va_start(ptr, address);
//
//	std::string phoneNumber = "0";
//	while(phoneNumber != "-1")
//	{
//
//		newStudent.phoneNumber.insert(phoneNumber);
//		phoneNumber = va_arg(ptr, std::string);
//		std::cout<<phoneNumber<<std::endl;
//	}
//	va_end(ptr);
//	this->student.push_back(newStudent);
//
//}


//struct stu PhoneBook::Search(std::string name)
//{
//	return students[0];
//}






bool PhoneBook::CheckNameExist(std::string name)
{
	auto search = students.find(name);
	if(search != students.end())
	{
		return true;
	}
	else
	{
		return false;
	}
}


void PhoneBook::AddPhoneNumberByName(std::string name, std::string phoneNumber)
{
	auto search = students.find(name);
	if(search != students.end())
	{
		search->second.phoneNumber.push_back(phoneNumber);
	}
	else	// not find name
	{
		AddStudent(name, "", phoneNumber);
	}

}

int PhoneBook::AddStudent(std::string name, std::string address, std::vector<std::string> phoneNumber)
{
	if (CheckNameExist(name))
	{
		return SAME_NAME;
	}


	else	// new name
	{
		struct stu newStudent;
		newStudent.name = name;
		newStudent.address = address;
		newStudent.phoneNumber = phoneNumber;

		students.insert(std::map<std::string, struct stu>::value_type(name, newStudent));//add student info
		phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name)); 	//add phone2name
	}
}



PhoneBook::~PhoneBook()
{

}


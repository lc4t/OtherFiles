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

	bool exitFlag = false;
	for(;!exitFlag;)
	{

		int inputCode = -1;
		std::string name,address,phoneNumber;
		std::cout << "There are <" << Count() << "> recode(s)" << std::endl;
		std::cout << "1) Add a new student {name,address,phone} " << std::endl;

		std::cout << "2) Find a student by {name} " << std::endl;
		std::cout << "3) Find a student by {phone} " << std::endl;

		std::cout << "4) Delete a student by {name} " << std::endl;
		std::cout << "5) Edit a student by {name} " << std::endl;

		std::cout << "6) Show name list" <<std::endl;
		std::cout << "7) Show all students' info" <<std::endl;
		std::cout << "8) Show phone list" <<std::endl;
#ifdef DEBUG
		std::cout << "9) Show phone to name" << std::endl;
#endif
		std::cout<< "0) Exit " << std::endl;
		std::cout << "Input number for what you want to do: ";

		std::cin >>inputCode;

		switch(inputCode)
		{
			case 1:
				name = InputName();
				address = InputAddress();
				phoneNumber = InputPhoneNumber();
				AddStudent(name, address, phoneNumber);
				break;
			case 2:
				name = InputName();
				PrintInfoByName(name);
				break;
			case 3:
				phoneNumber = InputPhoneNumber();
				PrintInfoByName(GetNameByPhoneNumber(phoneNumber));
				break;
			case 4:
				name = InputName();
				DeleteStudent(name);
			case 5:
				name = InputName();
				EditMode(name);
			case 6:
				ShowNameList();
				break;
			case 7:
				ShowAllInfo();
				break;
			case 8:
				ShowPhoneList();
				break;
#ifdef DEBUG
			case 9:
				ShowPhone2Name();
				break;
#endif
			case 0:
				exitFlag = true;
		}
	}
}


int PhoneBook::Count()
{
	return students.size();
}


void PhoneBook::AddStudent(std::string name, std::string address, std::string phoneNumber)
{
	CHANGE_INPUT_PHONE_NUMBER
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
//			 if(CheckPhoneNumberExist(phoneNumber))
//			 {
//				 phoneNumber = ChangeInputPhoneNumber();
//			 }

			 AddPhoneNumberByName(name, phoneNumber);
		}
			// add phoneNumber
	}
	else	// new name
	{
		struct stu newStudent;
		newStudent.name = name;
		newStudent.address = address;
		newStudent.phoneNumber.insert(phoneNumber);

		students.insert(std::map<std::string, struct stu>::value_type(name, newStudent));//add student info
		phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name)); 	//add phone2name
	}


}


void PhoneBook::AddPhone2Name(std::string phoneNumber, std::string name)
{
	// who use it should KEEP the phoneNumber not in phoneList
	// should have check for the phoneNumber not in phoneList
	if (phoneNumber != NONE_PHONENUMBER)
	{
		phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name));
	}


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
		return search->second;
	}
	else
	{
		return  NOT_FOUND;
	}
}


void PhoneBook::PrintInfoByName(std::string name)
{
	if (name == NOT_FOUND)
	{
		std::cout << "NOT FOUND" << std::endl;
		return ;
	}
	struct stu student = GetInfoByName(name);
	if(student.name != "")
	{
		std::cout<<START_STUDENT_INFO<<std::endl;
		std::cout<<"name: "<<student.name<<std::endl;
		std::cout<<"address:"<<student.address<<std::endl;
		std::cout<<"phone(s): ";
		for (auto it : student.phoneNumber)
			{
				std::cout<<it<<",";
			}
		std::cout<<std::endl<<END_STUDENT_INFO<<std::endl;
	}



}


void PhoneBook::EditMode(std::string name)
{
	std::cout<<IN_EDIT_MODE<<std::endl;
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
			if (name != newData)
			{
				AddStudent(newData, students[name].address, students[name].phoneNumber);
				DeleteStudent(name);
			}
			return;

		case 2:
			std::cout<<"Input a new address: "<<std::endl;
			std::cin>>newData;
			ChangeAddress(name, newData);
			break;
		case 3:
			int count = GetCountOfPhoneNumbers(name);
			int i = 0, code = -1;;	// i for phoneNumbers, code for input
			std::cout<<"There are(is) "<<count<<" phone number(s)."<<std::endl;

			std::string phoneNumbersArray[count];

			for(auto it : students[name].phoneNumber)
			{
				phoneNumbersArray[i] = it;
				std::cout<< ++i << ") " << it << std::endl;
			}

			std::cout<<"Input the number of phone to change: ";

			std::cin>>code;
			code --;
			std::cout<<"Input the new phone number: ";
			std::cin>>newData;
			ChangePhoneNumbers(name, phoneNumbersArray[i], newData);
			break;
	}
	std::cout << EXIT_EDIT_MODE << std::endl;
}


void PhoneBook::DeleteStudent(std::string name)
{
		//delete list of phone
		for (auto it : students[name].phoneNumber)
		{
			phone2name.erase(it);
		}
		students.erase(name);

}

int PhoneBook::GetCountOfPhoneNumbers(std::string name)
{
	return students[name].phoneNumber.size();
}

void PhoneBook::ChangePhoneNumbers(std::string name, std::string oldPhoneNumber, std::string phoneNumber)
{
	CHANGE_INPUT_PHONE_NUMBER

	auto search = students[name].phoneNumber.find(oldPhoneNumber);
	phone2name.erase(*search);
	phone2name.insert(std::map<std::string, std::string>::value_type(phoneNumber, name));

	students[name].phoneNumber.erase(*search);
	students[name].phoneNumber.insert(phoneNumber);



}

void PhoneBook::ChangeAddress(std::string name, std::string address)
{
	students[name].address = address;
}


struct stu PhoneBook::GetInfoByName(std::string name)
{
	// name not be NOT_FOUND
	auto search = students.find(name);
	if(search != students.end())
	{
		return search->second;
	}
	else
	{
		std::cout << "Do you want to add this new student?(Yes/No)" << std::endl;
		std::string inputString = "";
		std::cin >> inputString;
		if (inputString == "Yes")
		{
			std::string address, phoneNumber;
			std::cout << "Please input address for " << name << " :";
			std::cin >> address;
			std::cout << "Please input phone number for " << name << " :";
			std::cin >> phoneNumber;
			std::cout << "Forward to add " << name << std::endl;
			AddStudent(name, address, phoneNumber);
		}
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

std::string PhoneBook::InputName()
{
	std::string name;
	std::cout << "Please input a name: ";
	std::cin >> name;
	return name;
}
std::string PhoneBook::InputAddress()
{
	std::string address;
	std::cout << "Please input an address: ";
	std::cin >> address;
	return address;
}
std::string PhoneBook::InputPhoneNumber()
{
	std::string phoneNumber;
	std::cout << "Please input a phone number: ";
	std::cin >> phoneNumber;


	return phoneNumber;
}

void PhoneBook::ShowNameList()
{
	for (auto it : students)
	{
		std::cout << it.first << std::endl;
	}
}
void PhoneBook::ShowAllInfo()
{
	for (auto it : students)
	{
		PrintInfoByName(it.first);
	}

}
void PhoneBook::ShowPhoneList()
{
	for (auto it : phone2name)
	{
		std::cout << it.first << std::endl;
	}
}
void PhoneBook::ShowPhone2Name()
{
	for (auto it : phone2name)
	{
		std::cout << it.first << " -> " << it.second << std::endl;
	}
}


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


bool PhoneBook::CheckPhoneNumberExist(std::string phoneNumber)
{
	if (phoneNumber == NONE_PHONENUMBER)
	{
		return false;
	}
	auto search = phone2name.find(phoneNumber);
	if(search == phone2name.end())
	{
		return false;
	}
	else
	{
		return true;
	}
}


std::string PhoneBook::ChangeInputPhoneNumber()
{
	std::string inputPhoneNumber = NONE_PHONENUMBER;
	std::cout<<"The phone number is exist, please input another one(phone number/No): ";
	std::cin >> inputPhoneNumber;
	if (inputPhoneNumber != "No")
	{
		return inputPhoneNumber;
	}
	else
	{
		return NONE_PHONENUMBER;
	}
}

void PhoneBook::AddPhoneNumberByName(std::string name, std::string phoneNumber)
{
	auto search = students.find(name);
	if(search != students.end())
	{
		search->second.phoneNumber.insert(phoneNumber);
		AddPhone2Name(phoneNumber, name);			// for phone2name list
	}
	else	// not find name
	{
		AddStudent(name, "", phoneNumber);		// the phone is not exist, add a student
	}

}

int PhoneBook::AddStudent(std::string name, std::string address, std::set<std::string> phoneNumber)
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
		for (auto it : phoneNumber)
		{
			phone2name.insert(std::map<std::string, std::string>::value_type(it, name)); 	//add phone2name
		}

		return SUCCESS;
	}
}



PhoneBook::~PhoneBook()
{
	std::cout << "Your leave the phonebook,bye~~!" << std::endl;
}


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

}



void PhoneBook::AddStudent(std::string name, std::string address, std::string phoneNumber)
{
	struct stu newStudent;
	newStudent.name = name;
	newStudent.address = address;
	std::cout<<address;
	newStudent.phoneNumber.insert(phoneNumber);
	this->student.push_back(newStudent);
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


struct stu PhoneBook::Sea	rch(std::string name)
{
	return student[0];
}

int PhoneBook::Count()
{
	return student.size();
}






PhoneBook::~PhoneBook()
{

}


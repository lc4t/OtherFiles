/*
 * PhoneBook.h
 *
 *  Created on: 2015年9月7日
 *      Author: lc4t
 */

#ifndef INCLUDE_PHONEBOOK_H_
#define INCLUDE_PHONEBOOK_H_

#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <set>
#include <cstdarg>	// for phoneNumber

struct stu
{
	std::string name;
	std::string address;
	std::set<std::string> phoneNumber;
};


class PhoneBook
{
public:
	PhoneBook();
	int Count();	//count for all student
//	void AddStudent2(std::string name, std::string address, ...);	//Can't run
	void AddStudent(std::string name, std::string address, std::string phoneNumber);
	struct stu Search(std::string name);


	virtual ~PhoneBook();
private:
	std::vector<struct stu> student;
};

#endif /* INCLUDE_PHONEBOOK_H_ */

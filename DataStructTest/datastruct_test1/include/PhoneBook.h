/*
 * PhoneBook.h
 *
 *  Created on: 2015年9月7日
 *      Author: lc4t
 */

#ifndef INCLUDE_PHONEBOOK_H_
#define INCLUDE_PHONEBOOK_H_

#define NOT_FOUND "-1"
#define SAME_NAME 0x1

#include <map>
#include <set>
#include <list>
#include <string>
#include <vector>
//#include <cstdarg>	// for phoneNumber
#include <iostream>
#include <iterator>

struct stu
{
	std::string name;
	std::string address;
	std::vector<std::string> phoneNumber;
};



class PhoneBook
{
	/*
	 * AddStudent first,
	 * find by name: GetInfoByName(), return a struct stu.
	 * find by phone:GetInfoByPhoneNumber(). It will do self->GetNameByPhoneNumber()->GetInfoByName()
	 *
	 * if not match the name or the phone
	 */
public:
	PhoneBook();
	int Count();	//count for all student
//	void AddStudent2(std::string name, std::string address, ...);	//Can't run
	void AddStudent(std::string name, std::string address, std::string phoneNumber);	//add a student info
	void AddPhone2Name(std::string phoneNumber, std::string name);	//add phone number,map to a name
//	void AddPhone2List(std::string phoneNumber);	//for sort the whole phone numbers
	std::string GetNameByPhoneNumber(std::string phoneNumber);		// search: phone -> name
	void PrintInfoByName(std::string name);

	void EditMode(std::string name);
	void DeleteStudent(std::string name);



	int GetCountOfPhoneNumbers(std::string name);
	void ChangePhoneNumbers(std::string name, int index, std::string phoneNumber);
	void ChangeAddress(std::string name, std::string address);

	struct stu GetInfoByName(std::string name);
	struct stu GetInfoByPhoneNumber(std::string phoneNumber);

	virtual ~PhoneBook();

	struct stu noneStudent;
protected:

	bool CheckNameExist(std::string name);
	void AddPhoneNumberByName(std::string name, std::string phoneNumber);
	void AddStudent(std::string name, std::string address, std::vector<std::string> phoneNumber);
	std::map<std::string, struct stu> students;		//  map <name, studentInfo>, for match by O(lgn)
	std::map<std::string, std::string> phone2name; 	//  map <phoneNumber,name>,for match by O(lgn)
//	std::vector<std::string> phoneList;				//It will use by sort, IT designed add by SORTED (add:O(lgn))


};

#endif /* INCLUDE_PHONEBOOK_H_ */

/*
 * PhoneBook.h
 *
 *  Created on: 2015年9月7日
 *      Author: lc4t
 */

#ifndef INCLUDE_PHONEBOOK_H_
#define INCLUDE_PHONEBOOK_H_

//#define DEBUG

#define NOT_FOUND "-1"
#define SAME_NAME 0x1
#define SUCCESS 0x10
#define NONE_PHONENUMBER "434355449c562a6f63972d72e3abfcc3"
#define START_STUDENT_INFO 	"<-*******Current Student Info*******->"
#define END_STUDENT_INFO   	"<-*******  End Student Info  *******->"
#define IN_EDIT_MODE	 	"<-*******      Edit Mode     *******->"
#define EXIT_EDIT_MODE	 	"<-*******   Exit Edit Mode   *******->"

#define CHANGE_INPUT_PHONE_NUMBER while(CheckPhoneNumberExist(phoneNumber)) \
									 {\
										 phoneNumber = ChangeInputPhoneNumber();\
									 }

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
	std::set<std::string> phoneNumber;
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
	std::string GetNameByPhoneNumber(std::string phoneNumber);		// search: phone -> name
	void PrintInfoByName(std::string name);

	void EditMode(std::string name);
	void DeleteStudent(std::string name);



	int GetCountOfPhoneNumbers(std::string name);	// get the student's  COUNT of phones
	void ChangePhoneNumbers(std::string name, std::string oldPhoneNumber, std::string phoneNumber);	// Change exist phone to new one
	void ChangeAddress(std::string name, std::string address);	// Change exist address to new one

	struct stu GetInfoByName(std::string name);
	struct stu GetInfoByPhoneNumber(std::string phoneNumber);

	virtual ~PhoneBook();

	struct stu noneStudent;
protected:
	std::string InputName();
	std::string InputAddress();
	std::string InputPhoneNumber();

	void ShowNameList();
	void ShowAllInfo();
	void ShowPhoneList();
	void ShowPhone2Name();

	bool CheckNameExist(std::string name);
	bool CheckPhoneNumberExist(std::string phoneNumber);
	std::string ChangeInputPhoneNumber();			//user is inputing a phone number, if the phone is exist, tell user to change one
	void AddPhoneNumberByName(std::string name, std::string phoneNumber);
	int AddStudent(std::string name, std::string address, std::set<std::string> phoneNumber);
	std::map<std::string, struct stu> students;		//  map <name, studentInfo>, for match by O(lgn)
	std::map<std::string, std::string> phone2name; 	//  map <phoneNumber,name>,for match by O(lgn)
//	std::vector<std::string> phoneList;				//It will use by sort, IT designed add by SORTED (add:O(lgn))


};

#endif /* INCLUDE_PHONEBOOK_H_ */

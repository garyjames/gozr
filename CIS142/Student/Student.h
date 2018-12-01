#ifndef STUDENT_H_INCLUDED
#define STUDENT_H_INCLUDED

#include <iostream>
#include <string>

using namespace std;

class Student {

public:
    Student(); // Default constructor
    Student(int i); // Constructor with age
    Student(string n); // First name constructor
    Student(string f, string l); // First, Last name constructor
    Student(string f, string l, int i); // First, Last, Age constructor

    void setLastName(string n);
    void setFirstName(string n);
    void setAge(int i);

    string getLastName();
    string getFirstName();
    int getAge();

private:
    string last_name;
    string first_name;
    int age;
};

#endif // STUDENT_H_INCLUDED

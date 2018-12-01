#include <iostream>
#include <string>
#include "Student.h"

using namespace std;

Student::Student() {
    last_name = "";
    first_name = "";
    age = 0;
}

Student::Student(string f) {
    first_name = f;
    last_name = "";
    age = 0;
}

Student::Student(int n) {
    first_name = "";
    last_name = "";
    age = n;
}

Student::Student(string f, string l) {
    first_name = f;
    last_name = l;
    age = 0;
}

Student::Student(string f, string l, int i) {
    first_name = f;
    last_name = l;
    age = i;
}

void Student::setLastName(string n) {
    last_name = n;
}

void Student::setFirstName(string n) {
    first_name = n;
}

void Student::setAge(int i) {
    age = i;
}

string Student::getLastName() {
    return last_name;
}

string Student::getFirstName() {
    return first_name;
}

int Student::getAge() {
    return age;
}

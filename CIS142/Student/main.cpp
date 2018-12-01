#include <iostream>
#include <string>
#include "Student.h"

using namespace std;

int main()
{
    string firstName;
    string lastName;
    cout << "Hello world!" << endl;
    cout << "Enter first name: ";
    cin >> firstName;
    cout << "Enter last name: ";
    cin >> lastName;

    Student person1;
    person1.setLastName(lastName);
    person1.setFirstName(firstName);

    Student person2("Barney");
    Student person3("Fred", "Flintstone");
    Student person4("Bambam", "Rubble", 4);

    cout << "\n" << endl;

    cout << person1.getFirstName() << "\t" << person1.getLastName() << "\t" << person1.getAge() << endl;
    cout << person2.getFirstName() << "\t" << person2.getLastName() << "\t" << person2.getAge() << endl;
    cout << person3.getFirstName() << "\t" << person3.getLastName() << "\t" << person3.getAge() << endl;
    cout << person4.getFirstName() << "\t" << person4.getLastName() << "\t" << person4.getAge() << endl;

    return 0;
}

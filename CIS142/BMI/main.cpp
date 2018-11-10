#include <iostream>
#include "BMI.h"

using namespace std;

struct Person {
    string name;
    int height;
    float weight;
};

int main() {
    Person me;
    BMI myself;

    me.name = "Foo";
    me.height = 68;
    me.weight = 150;

    cout << "Enter your name";
    cin >> me.name;
    cout << "Enter your weight";
    cin >> me.weight;
    cout << "Enter your height";
    cin >> me.height;

    cout << "Hello " << me.name << "." << endl;
    cout << "Your height is " << me.height << endl;
    cout << "Your weight is " << me.weight << endl;


};

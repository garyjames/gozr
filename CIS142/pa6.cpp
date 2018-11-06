#include <iostream>

using namespace std;

int userin;

int main() {
    cout << "Please enter a number: ";
    cin >> userin;
    if (userin == 0) {
        cout << "Zero.\n" << endl;
    }
    else if (userin%2) {
        cout << "Odd number.\n" << endl;
    }
    else {
        cout << "Even number.\n" << endl;
    }
}

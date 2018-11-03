#include <iostream>

using namespace std;

int main() {

    int input;
    int sum = 0;

    do {
        // Please type in a number
        cout << "Enter a number (Enter 0 when done): ";
        cin >> input;
        
        // Add number to the sum
        sum = input + sum;
        // Please type in another number
    } while (input != 0);

    // Display number
    cout << "Hi I am done this is the sum:" << sum << endl;

    return 0;
}

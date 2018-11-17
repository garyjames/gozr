/*
Gary Galvez
CIS 142
Programming Assignment 7

Check Prime or Not in C++

    To check whether the number is a prime number or not a prime number in C++
    programming, you have to ask to the user to enter a number and start
    checking for prime number. If number is divisible by 2 or one less than
    that number (n-1), then the number is not prime number, otherwise it will
    be a prime number.

*/

#include <iostream>

using namespace std;
int user_number;
int factor_count = 0; // keep count of user_number factors

int main() {

    cout << "\nIs your number prime?\n\n" << endl;
    cout << "Enter a number (integer): ";
    cin >> user_number;

    // Starting at the user's number and counting down to 1,
    // apply the modulus operator to find a remainder, if it exists.
    //
    // Example
    //     500%500, 500%499, 500%498, ...
    //
    // When using the modulus operator (%), if the result is zero (0) then
    // you have evenly divided the number (i.e. no remainder). This will
    // indicate a factor of the number.
    //
    // If you only have 2 factors, then the number is prime.

    for (int i = user_number; 0 < i; i--) {
        if (user_number == 1) {
            factor_count++;
        }
        else if (user_number%i == 0) {
            factor_count++;
        }
    }
    cout << "Your number " << user_number << " has "
         << factor_count << " factors.\n" << endl;

    if (factor_count > 2) {
        cout << "\n" << user_number << " is NOT prime.\n" << endl;
    }
    else {
        cout << "\n" << user_number << " IS prime!\n" << endl;
    }

    return 0;
}

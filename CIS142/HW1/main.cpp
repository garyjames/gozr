/*
    CIS 142
    Gary Galvez
    10/11/2018

    This program will break down a number of cents given ( i.e. pennies are
    the lowest currency denominations ) into the larger currency denominations.
    For example, if 1258 cents are given then this application will return
    12 dollars, 2 quarters, 0 dimes, 1 nickels, and 3 pennies.
*/

#include <iostream>

using namespace std;

int main() {

    // Declare and initialize variables.
    int pennies, nickels, dimes, quarters, dollars, user_cents, balance;
    pennies = nickels = dimes = quarters = dollars = user_cents = balance = 0;

    // Prompt user to enter number of cents (pennies).
    cout << "Enter total cents: ";
    cin >> user_cents;

    // Sort user_cents into the greatest denominations.
    // Remove the quotient from the balance.
    balance = user_cents;
    if (balance > 100) {
        dollars = balance / 100;
        balance = balance - 100 * dollars;
    }
    if (balance > 25) {
        quarters = balance / 25;
        balance = balance - 25 * quarters;
    }
    if (balance > 10) {
        dimes = balance / 10;
        balance = balance - 10 * dimes;
    }
    if (balance > 5) {
        nickels = balance / 5;
        balance = balance - 5 * nickels;
    }
    pennies = balance;

    // Display the results.
    cout << user_cents << " cents breaks down into " \
         << dollars << " dollars, " << quarters << " quarters, " \
         << dimes << " dimes, " << nickels << " nickels, and " \
         << pennies << " pennies." << endl;

    return 0;
}

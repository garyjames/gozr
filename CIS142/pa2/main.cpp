/*
    CIS 142
    Gary Galvez
    10/12/2018

    Convert a given number of minutes into HH:MM:SS.ss format.

*/

# include<iostream>
# include <iomanip>      // std::setprecision

using namespace std;

int main () {

    // Vars
    float user_minutes, minutes_balance, seconds;
    int minutes_counter, decimal_part, hours, minutes;

    // Initialize vars
    minutes_counter = decimal_part = hours = minutes = 0;
    user_minutes = minutes_balance = seconds = 0;

    // Prompt user
    cout << "Enter the number of minutes: ";
    cin >> user_minutes;

    // Copy user_minutes to preserve original value
    minutes_balance = user_minutes;

    // Build integer from float to perform div and mod operations
    while (minutes_balance >= 1) {
        minutes_balance -= 1;
        minutes_counter++;
    }

    // Assign values from results
    hours = minutes_counter / 60;
    minutes = minutes_counter % 60;
    seconds = minutes_balance * 60;

    // Print results
    cout << user_minutes << " is equivalent to " \
         << hours << ":" << minutes << ":" << fixed << setprecision(2) << seconds << endl;

    return 0;
}

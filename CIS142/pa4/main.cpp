/*

CIS 142
Gary Galvez
10-28-2018


Programming assignment 4 (Function)

"Celsius and Fahrenheit temperature converter."

Let us start with an example execution of the program (user input is in bold):

This program will first ask the user how many conversions you would like to perform.

How many temperature conversions would you like to perform? 3

[#1] Enter the degree you want to convert: 44.492
Is this a Fahrenheit or Celsius temperature? [F/C]: F
44.49 F = 6.94 C

[#2] Enter the degree you want to convert: 212
Is this a Fahrenheit or Celsius temperature? [F/C]: F
212.00 F = 100.00 C

[#3] Enter the degree you want to convert: -100.55
Is this a Fahrenheit or Celsius temperature? [F/C]: C
-100.55 C = -148.99 F


************
Pseudo Code
************

int user_count
float user_temp
Fahrenheit2Celsius(user_temp)
Celsius2Fahrenheit(user_temp)

prompt user for number of conversions
get number of conversions

for number of conversions
    prompt user for a temperature
    get temperature (positive or negative float)
    prompt user for conversion type
    get conversion type (one character either F or C)
    apply correct formula
        case conversion
            F
                Fahrenheit2Celsius(user_temp)
            C
                Celsius2Fahrenheit(user_temp)
        print results


FUNCTIONS

Celsius2Fahrenheit(c)
    return c * 1.8 + 32

Fahrenheit2Celsius(f)
    return (f - 32) / 1.8

*/

#include <iostream>
#include <iomanip>    // std::setprecision

using namespace std;

int user_count;
float user_temp;
char user_temp_unit;
float result_temp;
char result_temp_unit;
float Celsius2Fahrenheit(float c);
float Fahrenheit2Celsius(float f);

int main()
{
    // prompt and get number of conversions from user
    cout << "Let's convert some temperatures from either Celsius to " \
         << "Fahrenheit or vice-versa!" << endl << endl;
    cout << "How many conversions would you like me to perform? ";
    cin >> user_count;

    // for number of conversions
    for (int i = user_count; i > 0; i--)
    {
        // prompt and get temperature from user
        cout << "Enter temperature to convert: ";
        cin >> user_temp;

        // get conversion type
        cout << "Is this temperature in Fahrenheit or Celsius? [F/C]: ";
        cin >> user_temp_unit;

        // apply correct formula
        switch (user_temp_unit)
        {
            case 'C':
            case 'c':
                result_temp = Celsius2Fahrenheit(user_temp);
                result_temp_unit = 'F';
                break;
            case 'F':
            case 'f':
                result_temp = Fahrenheit2Celsius(user_temp);
                result_temp_unit = 'C';
                break;
        }
        // print result
        cout << fixed << setprecision(2);
        cout << user_temp << " " << user_temp_unit << " = " \
             << result_temp << " " << result_temp_unit << endl;
    }
    return 0;
}

float Celsius2Fahrenheit(float c)
{
    return c * 1.8 + 32;
}

float Fahrenheit2Celsius(float f)
{
    return (f - 32) / 1.8;
}

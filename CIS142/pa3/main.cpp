/*

Programming Assignment 3

Calculate the volume and surface area (including the ends) of a cylinder.
Units are not required.

Inputs: radius and height of cylinder
Outputs: volume and surface area
         v = πrrh
         s = 2πr(r+h)
Display the results using 5 digits after the decimal point.

Testing: Run the program for the three cases shown below.

Case	r	h
1		5	10
2		25	5
3		34	2.6

*/

#include <iostream>
#include <iomanip>    // std::setprecision

using namespace std;

int main()
{
    // Variables,
    float pi = 3.14159;
    float radius, height, area, volume, surface_area;

    // prompt user for cylinder radius and height
    cout << "Enter cylinder's radius: ";
    cin >> radius;
    cout << "Enter the cylinder's height: ";
    cin >> height;

    // calculate area
    area = pi * radius * radius;

    // calculate volume
    volume = area * height;

    // calculate surface area
    surface_area = 2 * (pi * radius * height + area);

    // Print results
    cout << endl << "Volume = " << fixed << setprecision(5) << volume << endl;
    cout << "Surface Area = " << fixed << setprecision(5) << surface_area << endl;

    return 0;
}

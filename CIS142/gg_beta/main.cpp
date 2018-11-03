#include <iostream>

using namespace std;

int main()
{
    /* Design an algorithm to find the perimeter and area of a rectangle */

    int length, width, perimeter, area;

    /* Get the length of rectangle */
    cout << "What is the length of the rectangle?\n" << endl;
    cin >> length;
    cout << "You entered length " << length << endl;

    /* Get the width of rectangle */
    cout << "What is the width of the rectangle?\n" << endl;
    cin >> width;
    cout << "You entered width " << width << endl;

    /* Find the perimeter of rectangle */
    perimeter = 2*length + 2*width;

    /* Find the area of rectangle */
    area = length*width;

    /* Print the results */
    cout << "The perimeter of your rectangle is " << perimeter << endl;
    cout << "The area of your rectangle is " << area << endl;

    return 0;
}

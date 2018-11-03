#include <iostream>

using namespace std;

int main()
{
    int length, width, perimeter, area;

    cout << "What is the length of the rectangle?" << endl;
    cin >> length;
    cout << "What is the width of the rectangle?" << endl;
    cin >> width;

    perimeter = 2 * (length + width);
    area = length * width;

    cout << "Rectangle perimeter is " << perimeter << " and area is " << area << endl;

    return 0;
}

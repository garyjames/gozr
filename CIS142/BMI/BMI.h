#include <string>

using namespace std;

#ifndef BMI_H_INCLUDED
    #define BMI_H_INCLUDED

#endif // BMI_H_INCLUDED

class BMI {
    public:
        // Default Constructor
        BMI();

        // Overloaded Constructor
        BMI(string, int, float);
        BMI(string);

        // The tilde indicates the "de-constructor"
        ~BMI();

    private:
        string new_name;
        int new_height;
        float new_weight;
};

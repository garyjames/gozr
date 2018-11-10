// Function definitions

#include "BMI.h"

BMI::BMI() {
    new_height = 0;
    new_weight = 0.0;
};

BMI::BMI(string n, int h, float w) {
    new_name = n;
    new_height = h;
    new_weight = w;
};

BMI::BMI(string n) {
    new_name = n;
};

BMI::~BMI(){
};

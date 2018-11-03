/*
CIS 142
Gary Galvez
10/13/2018

A guessing program that will ask the user to guess a randomly generated
number
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    // Generate a random number
	int random_number, user_guess;
	srand(time(0));
    random_number = rand();


	// Prompt user to guess random_number
    cout << "Guess what number I'm thinking of . . . ";
	cin >> user_guess;

	// While user's guess is not equal to the random number
    while (user_guess != random_number) {

        cout << "Nice try but your guess is ";

        // Check whether user's guess is either greater than or
        // less than random_number.
        if (user_guess > random_number) {
            cout << "greater";
        }
        if (user_guess < random_number) {
            cout << "less";
        }

        // Prompt user with result and ask user to guess again
        cout << " than the number I'm thinking of. Try again . . ." << endl;
        cin >> user_guess;
    }

    // User has guessed the random number!
    cout << "Correct !!!!!!  Nice Job!!!" << endl;

    return 0;
}

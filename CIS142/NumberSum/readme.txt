/*
    This program will add an unknown amount of numbers from user input
and then display the sum.
*/


/*
    Prompt user with instructions.

    Enter numbers to be added to running total. When finished,
	enter zero (0) as your number to display running total.
*/
    cout << "Enter numbers to be added to running total." << endl;
	cout << "When finished, enter zero to display running total." << endl;

// Create variables for running total and user's input.
    float user_number, running_total;
	running_total = 0;

// Prompt user to enter their number.
    cout << "Enter a number (0 to end and display total): ";
	cin >> user_number;

// Repeat until user is finished (i.e. user_number is 0).
    while (user_number != 0)
	{
		// Add user_number to the running_total.
		running_total += user_number;
		cout << "Enter a number (0 to end and display total): ";
		cin >> user_number;
	}

// Display running_total.
    cout << "Your sum of numbers is " << running_total << endl;
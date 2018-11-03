/*
    This program will break down a number of cents given ( i.e. pennies are
	the lowest currency denominations ) into the larger currency denominations.
	For example, if 1258 cents are given then this application will return
	12 dollars, 2 quarters, 0 dimes, 1 nickels, and 3 pennies.
*/

// Prompt user with instructions.

// Declare and initialize variables.
    int pennies, nickels, dimes, quarters, dollars, cents_given;
    cents_given = pennies = nickels = dimes = quarters = dollars = 0;
	
// Get the number of cents (pennies) from the user.
    cout << "Enter total number of cents: ";
	cin >> cents_given;
	
// Sort out (divide) the pennies into their greatest denominations.
    dollars = cents_given/100;

// Display the results.
    cout << "This breaks down to " << dollars << " dollars, " << endl;
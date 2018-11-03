/*

Gary Galvez
CIS 142
Programming Assignment 5

ATM Machine Phase 1

In this assignment you will create a program that allows a user to do the following:

1) Create a bank account by supplying a user id and password.
2) Login using their id and password.
3) Quit the program.

Now if login was successful the user will be able to do the following:

1) Withdraw money.
2) Deposit money.
3) Request balance.
4) Quit the program.

If login was not successful (for example the id or password did not match) then the user will be taken back to the introduction menu.

// CODE STARTS HERE

       #include <iostream.h>
       #include <stdlib.h>

	// function prototypes
       void printIntroMenu();
       void printMainMenu();
       void start();
       void login();
       void createAccount();

       // global variable (use this variable to store the user’s menu selection)
       char menuInput;

       // the main function
       int main()
       {
       	// TO WRITE A WELCOME MESSAGE HERE

		// call the function start
		start();

		return 0;
       }

void printIntroMenu()
       {
       	// WRITE CODE HERE
       }

void printMainMenu()
       {
       	// WRITE CODE HERE
       }

       void start()
       {
       	// EXPLANATION OF CODE THAT GOES HERE IS BELOW
       }

       void createAccount()
       {
       	// PHASE 2
       }

       void login()
       {
       	// PHASE 2
       }

// CODE ENDS HERE


The function printIntroMenu() displays the following:

	Please select an option from the menu below:
    l -> Login
    c -> Create New Account
    q -> Quit

The function printMainMenu() displays the following menu:

    d -> Deposit Money
    w -> Withdraw Money
    r -> Request Balance
    q -> Quit

The function start() does the following:

    1) Displays the following message, “Please select an option from the menu below: ”
    2) Displays the introduction menu. Do this by calling the function you created earlier, printIntroMenu()
    3) Program halts and waits for the user to make their selection. Use the cin >> function to accomplish this step.
    4) Now use a switch statement to do the following:
        If the user types the character ‘l’ then the function login() is called
        If the user types the character ‘c’ then the function createAccount() is called.
        If the user types ‘q’ your program will terminate by calling the function exit(0)

*/

#include <iostream>
#include <cctype>

using namespace std;

char menuInput;
char user_id_input[32];
char user_pw_input[32];
char user_id[32];
char user_pw[32];

void printIntroMenu();
void start();

int main()
{
    start();
}

void printIntroMenu()
{
    cout << "(L) -> Login\n";
    cout << "(C) -> Create New Account\n";
    cout << "(Q) -> Quit\n\n";

}

void printMainMenu()
{
    cout << "(D) -> Deposit Money\n";
    cout << "(W) -> Withdraw Money\n";
    cout << "(R) -> Request Balance\n";
    cout << "(Q) -> Quit\n";
}

void start()
{
    cout << "Welcome to the Cold Hard Cash ATM !!\n\n";
    cout << "Please select an option from the menu below\n\n";
    cin >> menuInput;
    menuInput = toupper(menuInput); // ensure it is in upper case

    switch (menuInput)
    {
        case 'L':
            login();
            break;
        case 'C':
            createAccount();
            break;
        case 'Q':
            cout << "Quit!!!!!!!!!!!";
            break;
    }
}

void login()
{

}

void createAccount()
{

}

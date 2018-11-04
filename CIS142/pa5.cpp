/*

Gary Galvez
CIS 142
Programming Assignment 5 - ATM Machine

A program that allows a user to do the following:

    1) Create a bank account by supplying a user id and password.
    2) Login using their id and password.
    3) Quit the program.

Now if login was successful the user will be able to do the following:

    1) Withdraw money.
    2) Deposit money.
    3) Request balance.
    4) Quit the program.

If login was not successful (for example the id or password did not match) then
the user will be taken back to the introduction menu.

*/

#include <iostream>

using namespace std;

// vars
int authenticated = 0;
float balance = 0;
float user_input = 0;
char selection = '0';
char user_input_id[32];
char user_input_pw[32];
char user_id[32];
char user_pw[32];

// main function
void start();

// menu_intro and menu_main
// act as callers for all relevant "helper" functions
void menu_intro();
void menu_main();

// helper functions
void login();
void get_selection();
void create_account();
void print_menu_intro();
void print_menu_main();
void implement_intro_selection();
void implement_main_selection();
void withdraw();
void deposit();
void print_balance();




int main() {
    start();
}

void start() {
    cout << "Welcome to the Cold Hard Cash ATM !!\n\n";

    // Loop until user selects 'Q' to Quit
    while (1) {
        if ( !authenticated ) {
            menu_intro();
        }
        else {
            menu_main();
        }
    }
}

void menu_intro() {
    print_menu_intro();
    get_selection();
    implement_intro_selection();
}

void menu_main() {
    print_menu_main();
    get_selection();
    implement_main_selection();
}

void print_menu_intro() {
    cout << "\n\nSelect an option from menu below\n\n";
    cout << "(L) -> Login\n";
    cout << "(C) -> Create New Account\n";
    cout << "(Q) -> Quit\n\n";
}

void print_menu_main() {
    cout << "\n\nSelect an option from menu below\n\n";
    cout << "(D) -> Deposit Money\n";
    cout << "(W) -> Withdraw Money\n";
    cout << "(R) -> Request Balance\n";
    cout << "(Q) -> Quit\n\n";
}

void get_selection() {
    cin >> selection;
    selection = toupper(selection);  // force upper case for switch
}

void implement_intro_selection() {
    switch (selection) {
        case 'L':
            login();
            break;
        case 'C':
            create_account();
            break;
        case 'Q':
            exit(0);
    }
}

void implement_main_selection() {
    switch (selection) {
        case 'D':
            deposit();
            break;
        case 'W':
            withdraw();
            break;
        case 'R':
            print_balance();
            break;
        case 'Q':
            exit(0);
    }
}

void create_account() {
    cout << "Please enter your user name: ";
    cin >> user_id;
    cout << "Please enter your password: ";
    cin >> user_pw;
}

void login() {
    int failed = 0;

    cout << "Please login below\n\n";
    cout << "login: ";
    cin >> user_input_id;
    cout << "password: ";
    cin >> user_input_pw;

    for (int i=0; i < sizeof user_input_id; i++) {
        if (user_input_id[i] != user_id[i] || user_input_pw[i] != user_pw[i]) {
            failed = 1;
        }
    }
    if (failed) {
        cout << "\n\n******** LOGIN FAILED! ********\n\n" << endl;
    }
    else {
        authenticated = 1;
    }
}

void print_balance() {
    cout << "Your balance is $" << balance << endl;
}

void deposit() {
    cout << "Amount of deposit: $";
    cin >> user_input;
    balance += user_input;
}

void withdraw() {
    cout << "Amount of withdrawl: $";
    cin >> user_input;
    if (balance >= user_input) {
        balance -= user_input;
    }
    else {
        cout << "Not enough funds, nice try.";
    }
}

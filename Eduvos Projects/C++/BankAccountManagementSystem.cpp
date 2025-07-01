#include <iostream>
#include <string>
#include <limits>
#include <iomanip>
using namespace std;

// Optional: Clear screen function for better UI
void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

// Create an account
void createAccount(string &name, int &accountNumber, double &balance) {
    cout << "Enter your name: ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Safer flush
    getline(cin, name);

    cout << "Enter your account number: ";
    cin >> accountNumber;

    while (true) {
        cout << "Enter initial deposit (must be > 0): ";
        cin >> balance;
        if (balance > 0) break;
        cout << "Initial deposit has to be more than zero!\n";
    }

    cout << "Account created successfully!\n";
}

// Deposit money
void depositMoney(double &balance) {
    double amount;
    cout << "Enter deposit amount (> 0): ";
    cin >> amount;

    if (amount > 0) {
        balance += amount;
        cout << "Deposit successful. New balance: " << balance << "\n";
    } else {
        cout << "Deposit amount must be more than zero!\n";
    }
}

// Withdraw money
void withdrawMoney(double &balance) {
    double amount;
    cout << "Enter withdrawal amount (> 0): ";
    cin >> amount;

    if (amount > 0 && amount <= balance) {
        balance -= amount;
        cout << "Withdrawal successful. Amount: " << amount << "\n";
        cout << "New balance: " << balance << "\n";
    } else if (amount > balance) {
        cout << "Insufficient funds for this withdrawal!\n";
    } else {
        cout << "Withdrawal amount must be greater than zero!\n";
    }
}

// Check balance
void checkBalance(const double &balance) {
    cout << "Your current balance is: " << balance << "\n";
}

// Display account details
void displayAccountDetails(const string &name, const int &accountNumber, const double &balance) {
    cout << "Account Holder: " << name << "\n";
    cout << "Account Number: " << accountNumber << "\n";
    cout << "Current Balance: " << balance << "\n";
}

// Main program
int main() {
    string name;
    int accountNumber;
    double balance = 0;
    bool accountExists = false;
    int choice;

    cout << fixed << setprecision(2); // Format money values

    do {
        clearScreen(); // Optional: clears screen for a cleaner UI
        cout << "--- Welcome to MyBank ---\n";
        cout << "1. Create Account\n";
        cout << "2. Deposit Money\n";
        cout << "3. Withdraw Money\n";
        cout << "4. Check My Balance\n";
        cout << "5. Show My Account Details\n";
        cout << "6. Exit\n";
        cout << "Choose an option: ";
        cin >> choice;

        switch (choice) {
            case 1:
                createAccount(name, accountNumber, balance);
                accountExists = true;
                break;
            case 2:
                if (accountExists)
                    depositMoney(balance);
                else
                    cout << "No account found. Please create an account first.\n";
                break;
            case 3:
                if (accountExists)
                    withdrawMoney(balance);
                else
                    cout << "No account found. Please create an account first.\n";
                break;
            case 4:
                if (accountExists)
                    checkBalance(balance);
                else
                    cout << "You need to create an account to check your balance.\n";
                break;
            case 5:
                if (accountExists)
                    displayAccountDetails(name, accountNumber, balance);
                else
                    cout << "No account has been created yet.\n";
                break;
            case 6:
                cout << "Thank you for banking with us. Goodbye!\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }

        if (choice != 6) {
            cout << "\nPress Enter to continue...";
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cin.get();
        }

    } while (choice != 6);

    return 0;
}

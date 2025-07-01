#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

// Declaring constants
const double DISCOUNT_RATE = 0.10; // 10% discount
const double DISCOUNT_THRESHOLD = 100.00; // Discount applies if bill exceeds R100

const double COFFEE_PRICE = 15.00;
const double SANDWICH_PRICE = 30.00;
const double SALAD_PRICE = 25.00;
const double JUICE_PRICE = 10.00;
const double MUFFIN_PRICE = 20.00;
const double PIZZA_PRICE = 35.00;
const double SOUP_PRICE = 18.00;
const double BURGER_PRICE = 40.00;

// Struct to hold menu items
struct MenuItemType {
    string itemName;
    double itemPrice;
};

// Function to display the menu
void displayMenu(const MenuItemType menuItems[], int size) {
    cout << "Cafeteria Menu:\n";
    for (int i = 0; i < size; ++i) {
        cout << i + 1 << ". " << menuItems[i].itemName
             << " - R" << fixed << setprecision(2) << menuItems[i].itemPrice << endl;
    }
}

int main() {
    // Define menu items
    MenuItemType menuItems[8] = {
        {"Coffee", COFFEE_PRICE}, {"Sandwich", SANDWICH_PRICE}, {"Salad", SALAD_PRICE},
        {"Juice", JUICE_PRICE}, {"Muffin", MUFFIN_PRICE}, {"Pizza Slice", PIZZA_PRICE},
        {"Soup", SOUP_PRICE}, {"Burger", BURGER_PRICE}
    };

    // Getting customer details
    string firstName, lastName;
    cout << "Enter your name: ";
    cin >> firstName;
    cout << "Enter your surname: ";
    cin >> lastName;

    // Display menu
    displayMenu(menuItems, 8);

    // Order input
    int numItems, itemChoice;
    double totalBill = 0.0;

    cout << "How many items would you like to order (up to 8)? ";
    cin >> numItems;

    // Order selection and validation
    for (int i = 0; i < numItems; ++i) {
        cout << "Select item " << i + 1 << " (1-8): ";
        cin >> itemChoice;
        
        // Validate selection
        if (itemChoice >= 1 && itemChoice <= 8) {
            totalBill += menuItems[itemChoice - 1].itemPrice;
        } else {
            cout << "Invalid selection, please try again." << endl;
            --i; // Retry current item
        }
    }

    // Apply discount if applicable
    double discount = 0.0;
    if (totalBill > DISCOUNT_THRESHOLD) {
        discount = totalBill * DISCOUNT_RATE;
    }
    double finalBill = totalBill - discount;

    // Display total, discount, and final bill
    cout << fixed << setprecision(2);
    cout << "\nTotal Bill: R" << totalBill << endl;
    if (discount > 0) {
        cout << "Discount applied: R" << discount << endl;
    } else {
        cout << "No discount applied." << endl;
    }
    cout << "Final Bill: R" << finalBill << endl;

    // Writing to file
    ofstream outFile("CafeteriaBill.txt");
    if (outFile) {
        outFile << "Customer: " << firstName << " " << lastName << endl;
        outFile << "Final Bill: R" << finalBill << endl;
        cout << "The bill has been written to CafeteriaBill.txt." << endl;
        outFile.close();
    } else {
        cerr << "Error: Could not open the file." << endl;
    }

    return 0;
}

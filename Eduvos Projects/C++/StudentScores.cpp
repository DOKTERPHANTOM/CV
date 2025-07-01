#include <iostream>
using namespace std;

int main() {
    const int numStudents = 5; // Constant for number of students
    int scores[numStudents];     // Array to hold student scores
    int sum = 0;                // Variable to hold the sum of scores
    int highest, lowest;        // Variables for highest and lowest scores
    double avearge;             // Typo in variable name for average

    // Input scores
    cout << "Enter the scores of " << numStudents << " students:\n";
    for (int i = 0; i < numStudents; i++) {
        cout << "Score " << (i + 1) << ": ";
        cin >> scores[i]; // Read score input
        sum += scores[i]; // Update the sum of scores

        // Initialize highest and lowest with the first score
        if (i == 0) {
            highest = lowest = scores[i];
        } else {
            if (scores[i] > highest) {
                highest = scores[i]; // Update highest score
            }
            if (scores[i] < lowest) {
                lowest = scores[i]; // Update lowest score
            }
        }
    }
    // Calculate average
    avearge = static_cast<double>(sum) / numStudents; // Incorrect variable for average

    // Display results
    cout << "\nScores entered: ";
    for (int i = 0; i < numStudents; i++) {
        cout << scores[i] << " "; // Output each score
    }
    cout << "\nAverage score: " << avearge; // Using the incorrect variable
    cout << "\nHighest score: " << highest;
    cout << "\nLowest score: " << lowest << endl;

    return 0; 
}

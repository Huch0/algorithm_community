#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int getMenuTime(char menu) {
    switch (menu) {
    case 'A': return 1;
    case 'B': return 2;
    case 'C': return 3;
    case 'D': return 4;
    case 'E': return 5;
    case 'F': return 7;
    case 'G': return 10;
    case 'H': return 12;
    case 'I': return 14;
    case 'J': return 15;
    }
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, char>> reservations;
    for (int i = 0; i < n; ++i) {
        int time;
        char menu;
        cin >> time >> menu;
        reservations.push_back({ time, menu });
    }

    // Sort reservations based on entrance time
    sort(reservations.begin(), reservations.end());

    // Use a priority queue to keep track of table availability
    priority_queue<int, vector<int>, greater<int>> tables;

    int totalTables = 0;

    for (const auto& reservation : reservations) {
        int menuTime = getMenuTime(reservation.second);

        if (!tables.empty() && tables.top() <= reservation.first) {
            // Assign the table to the customer
            tables.pop();
            tables.push(reservation.first + menuTime);
        }
        else {
            // No available table, increment the total tables
            ++totalTables;
            tables.push(reservation.first + menuTime);
        }
    }

    cout << totalTables << endl;

    return 0;
}

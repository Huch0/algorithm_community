// Add any additional header files freely
#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

// Returns menu serving time of each menu
int getMenuTime(char menu){
    switch(menu){
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

// Your program here

class Customer {
    int entranceTime_;
    char menu_;

public:
    Customer(int entranceTIme, char menu) : entranceTime_(entranceTIme), menu_(menu) {};
    ~Customer() = default;

    [[nodiscard]] int getEntranceTime() const {
        return entranceTime_;
    }

    [[nodiscard]] char getMenu() const {
        return menu_;
    }

    [[nodiscard]] int getOutTime() const {
        return entranceTime_ + getMenuTime(menu_) - 1;
    }
};

class CustomerIsLarger {
public :
    bool operator() (const Customer& c1, const Customer& c2) const {
        return c1.getEntranceTime() > c2.getEntranceTime();
    }
};
class Table {
    int endTime_;

public:
    explicit Table(int endTime) : endTime_(endTime) {};

    [[nodiscard]] int getEndTime() const {
        return endTime_;
    }

    void setEndTime(int newEndTime) {
        endTime_ = newEndTime;
    };
};

int main () {
    priority_queue<Customer, vector<Customer>, CustomerIsLarger> customerMinHeap;

    int customers;
    cin >> customers;

    // Get Customers and push to Priority Queue
    int entranceTime;
    char menu;
    for (int i = 0; i < customers; i++) {
        cin >> entranceTime >> menu;
        Customer newCustomer = Customer(entranceTime, menu);

        customerMinHeap.push(newCustomer);
    }

    vector<Table> tables;

    // Iterate through customerMinHeap
    while (!customerMinHeap.empty()) {
        Customer currentCustomer = customerMinHeap.top();
        customerMinHeap.pop();

        // Find available table
        auto it = tables.begin();

        while (it != tables.end()) {
            if (it->getEndTime() < currentCustomer.getEntranceTime())
                break;
            it.operator++();
        }


        if (it != tables.end()) {
            // Assign customer to an existing table
            it->setEndTime(currentCustomer.getOutTime());
        } else {
            // There is no available table
            // Create a new Table
            tables.emplace_back(currentCustomer.getOutTime());
        }
    }

    // Print the number of Tables
    cout << tables.size() << endl;

    return 0;
}
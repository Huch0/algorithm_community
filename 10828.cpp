#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <utility>
#include <vector>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main() {
    int N;
    stack<int> numbers;
    string command;
    int num;
    cin >> N;
    while (N) {
        N--;
        cin >> command;
        switch (command[0]) {
        case 'p':
            if (command[1] == 'u') {
                cin >> num;
                numbers.push(num);
            }
            else {
                if (numbers.empty()) {
                    cout << -1 << endl;
                }
                else {
                    cout << numbers.top()<<endl;
                    numbers.pop();
                } 
            }
            break;
        case 's':
            cout << numbers.size() << endl;
            break;
        case 'e':
            if (numbers.empty()) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
            break;
        case 't':
            if (numbers.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << numbers.top() << endl;
            } 
            break;
        }
    }
    cin >> N;
}
#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>

using namespace std;



int main() {
    int N;
    cin >> N;
    string PS;
    int i;
    int NVPS;
    while (N) {
        N--;
        NVPS = 0;
        cin >> PS;
        stack<char> myStack;
        for (i = 0; i < PS.length(); i++) {
            if (PS[i] == '(') {
                myStack.push(PS[i]);
            }
            else {
                if (myStack.empty()) {
                    NVPS = 1;
                    break;
                }
                myStack.pop();
            }
        }
        if (NVPS) {
            cout << "NO" << '\n';
        }
        else {
            if (myStack.empty()) {
                cout << "YES" << '\n';
            }
            else {
                cout << "NO" << '\n';
            }
        }
    }
    cin >> N;
}
#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(void) {
    string s; cin >> s;
    stack<char> a;
    bool flag = true;
    int num = 1, sum = 0;

    for (int i = 0; flag && i < s.size(); i++) {
        if (s[i] == ')') {
            if (a.empty() || a.top() != '(') flag = false;
            num /= 2;
            a.pop();
        }

        else if (s[i] == ']') {
            if (a.empty() || a.top() != '[') flag = false;
            num /= 3;
            a.pop();
        }

        else if (i == s.size()-1) flag = false;

        else if (s[i] == '(') {
            num *= 2;
            a.push(s[i]);
            if (s[i+1] == ')') sum += num;
        }

        else {
            num *= 3;
            a.push(s[i]);
            if (s[i+1] == ']') sum += num;
        }
    }
    if (flag && a.empty()) cout << sum;
    else cout << 0;
    return 0;
}
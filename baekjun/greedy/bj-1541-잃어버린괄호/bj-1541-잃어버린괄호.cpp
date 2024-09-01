#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string str; cin >> str;
    str.push_back('+');

    bool minus = false;
    int sum = 0;
    int temp = 0;
    for ( char c : str ) {
        if( c == '+' || c == '-' ) {
            if( minus ) sum -= temp;
            else sum += temp;
            temp = 0;
        }
        if( c == '-' ) minus = true;
        if( c >= '0' && c <= '9' ) temp = temp * 10 + (c - '0');
    }

    cout << sum << endl;
}
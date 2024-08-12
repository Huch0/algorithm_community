#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string str; cin >> str;
    char target = str.front();
    bool isZero = (target == '0' ? true : false);
    int count = 0;
    while (true) {
        auto it = find_if(str.begin(), str.end(), [target](char c) { return c != target; });
        if( it == str.end() ) break;
        auto it2 = find_if(str.rbegin(), str.rend(), [target](char c) { return c != target; }).base();
        for (auto i=it; i!=it2; i++) {
            if( *i == target ) *i = (isZero) ? '1' : '0';
            else *i = target;
        }
        count++;
    }
    cout << count;
}

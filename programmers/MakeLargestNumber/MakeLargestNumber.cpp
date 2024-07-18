#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

string solution(string number, int k) {
    for (int i=0; i<number.length()-k && k!=0; i++) {
        auto it = max_element(number.begin()+i, number.begin()+i+k+1);
        if( it != number.begin()+i ) {
            number.erase(number.begin()+i, it);
            k -= distance(number.begin()+i, it);
        }
    }
    if( k != 0 ) number = number.substr(0, number.length()-k);
    return number;
}
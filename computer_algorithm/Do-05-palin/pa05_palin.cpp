#include <iostream>
#include <string>
#include <vector>
using namespace std;

int printPalinLength(string s, int direction) {
    int n = s.size();
    int left = 0, right = n-1;
    int counter = 0;
    while (left < right) {
        if( (left == 0 && right == n-1) && s[left] != s[right] ) return 0;
        if( direction != 0 && s[left] != s[right] && counter == 2 ) {
            if( direction == 1 ) {
                while (s[left] != s[right] && left < right) left++;
                if( left <= right ) return printPalinLength(s.substr(left, right-left+1), 1);
                else return 0;
            }
            if (direction == 2) {
                while (s[left] != s[right] && left < right) right--;
                if( left <= right ) return printPalinLength(s.substr(left, right-left+1), 2);
                else return 0;
            }
        }
        if( direction != 0 && counter > 2 && s[left] != s[right] ) return 0;
        if( s[left] != s[right] && direction == 0 ) {
            int newLeft = left, newRight = right;
            int leftSub, rightSub;
            while (s[left] != s[right]) left ++;
            if( left <= right ) leftSub = counter + printPalinLength(s.substr(left, right-left+1), 1);
            while (s[newLeft] != s[newRight]) newRight--;
            if( newLeft <= newRight ) rightSub = counter + printPalinLength(s.substr(newLeft, newRight-newLeft+1), 2);
            return max(leftSub, rightSub);
        }
        left++; right--;
        counter+=2;
    }
    if( left == right ) counter++;
    return counter;
}

int main() {
    int n; cin >> n;
    vector<string> palin(n);
    for (int i=0; i<n; i++) cin >> palin[i];
    for (int i=0; i<n; i++) cout << printPalinLength(palin[i], 0) << endl;
    
    return 0;
}

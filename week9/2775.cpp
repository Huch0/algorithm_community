#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int members(int k, int n) {
    if (k == 0) {
        return n;
    }
    if(n==1){
        return 1;
    }
    
    return members(k - 1, n) + members(k, n - 1);
}
int main() {
    int T;
    cin >> T;
    int k;
    int n;
    while (T) {
        cin >> k;
        cin >> n;
        cout << members(k, n) << '\n';
        T--;
    }
    cin >> T;
}
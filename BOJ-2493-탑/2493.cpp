#include <iostream>
#include <stack>
#include <utility>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0), cin.tie(0);

    stack<pair<int,int>> s;
    s.push({1e8+1, 0});
    int n, h, i;
    cin >> n;

    for (i = 1; i <= n; i++) {
        cin >> h;
        while (s.top().first < h) s.pop();
        cout << s.top().second << ' ';
        s.push({h,i});
    }
    return 0;
}
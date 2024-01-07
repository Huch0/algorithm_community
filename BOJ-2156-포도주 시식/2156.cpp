#include <bits/stdc++.h>
using namespace std;

int dp[10001][3];

int main() {
    int n, t; cin >> n;
    vector<int> v;
    for (int i = 0; i < n; i++) {
        cin >> t; v.push_back(t);
    }

    dp[0][1] = v[0];
    if (n > 1) {
        dp[1][0] = v[0];
        dp[1][1] = v[1];
        dp[1][2] = v[0] + v[1];
    }

    for (int i = 2; i < n; i++) {
        dp[i][0] = max({dp[i-1][0], dp[i-1][1], dp[i-1][2]});
        dp[i][1] = max({dp[i-2][0], dp[i-2][1], dp[i-2][2]}) + v[i];
        dp[i][2] = dp[i-1][1] + v[i];
    }
    
    cout << max({dp[n-1][0], dp[n-1][1], dp[n-1][2]});
}

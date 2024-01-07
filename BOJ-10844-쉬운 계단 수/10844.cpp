#include <bits/stdc++.h>
using namespace std;

const int DIV = 1000000000;
int n, dp[101][10];

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i = 1; i <= 9; i++) dp[1][i] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i][0] = dp[i-1][1];
        dp[i][9] = dp[i-1][8];
        for (int j = 1; j <= 8; j++) dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % DIV;
    }

    int ans = 0;
    for (int i = 0; i <= 9; i++) ans = (ans + dp[n][i]) % DIV;
    cout << ans;
}
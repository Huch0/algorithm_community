#include <bits/stdc++.h>
using namespace std;

int n, a[501][501], ans;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) cin >> a[i][j];
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) a[i][j] += a[i-1][j];
            else a[i][j] += max(a[i-1][j], a[i-1][j-1]);
        }
    }

    for (int i = 0; i < n; i++) ans = max(ans, a[n-1][i]);
    cout << ans;
}
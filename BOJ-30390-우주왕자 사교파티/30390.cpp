#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    ll a, b, k, n, f1, f2;
    cin >> a >> b >> k;
    n = a + b;
    ll ans = 1;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            f1 = i; f2 = n/i;
            if (a % f1 <= k || b % f1 <= k) ans = max(ans, f1);
            if (a % f2 <= k || b % f2 <= k) ans = max(ans, f2);
        }
    }
    cout << ans;
}
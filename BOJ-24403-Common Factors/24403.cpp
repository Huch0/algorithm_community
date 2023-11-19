#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};

ll gcd(ll a, ll b) {
    while (b) {
        ll t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    ll n; cin >> n;
    int idx = -1;
    ll denom = 1;
    while ((++idx) < 15 && denom * primes[idx] <= n) denom *= primes[idx];

    ll numer = denom;
    for (int i = 0; i < idx; i++) numer = numer / primes[i] * (primes[i]-1);
    numer = denom - numer;

    ll G = gcd(numer, denom);
    cout << numer/G << '/' << denom/G;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int N, S;
    cin >> N >> S;
    vector<int> v(N+1,0);
    for (int i = 1; i <= N; i++) {
        cin >> v[i];
        v[i] += v[i-1];
    }

    int start = 0, end = 0;
    int cmp = N+1;

    while (end++ < N) {
        if (v[end] - v[start] < S) continue;
        while (v[end] - v[start] >= S) start++;
        if (end - start + 1 < cmp) cmp = end - start + 1;
    }
    if (cmp == N+1) cout << 0;
    else cout << cmp;
}
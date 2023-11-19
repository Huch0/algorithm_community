#include <bits/stdc++.h>
using namespace std;

int dim[2][3001], dp[3001][3001], mia[3001];
int N, M, K, G, Y, L, X;

void init() {
    cin >> N >> M >> K;
    for (int i = 0; i < K; i++) {
        cin >> G >> Y;
        dim[0][i] = G;
        dim[1][i] = Y;
    }

    cin >> L;
    for (int i = 0; i < L; i++) {
        cin >> X;
        mia[X] = 1;
    }
    dp[0][M] = 1;
}

void solve() {
    for (int i = 0; i < K; i++) {
        for (int j = 0; j < N; j++) {
            if (!dp[i][j]) continue;
            for (int k = 0; k < 2; k++) {
                int t = (j + dim[k][i]) % N;
                if (!mia[t]) dp[i+1][t] = 1;
            }
        }
    }

    if (dp[K][0]) cout << "utopia";
    else cout << "dystopia";
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    init();
    solve();
}
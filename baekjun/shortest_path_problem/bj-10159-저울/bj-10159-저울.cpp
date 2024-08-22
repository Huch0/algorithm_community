#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<vector<bool>> adj;

void floydWarshall() {
    for (int k=1; k<=N; k++) {
        for (int i=1; i<=N; i++) {
            for (int j=1; j<=N; j++) {
                if( adj[i][k] && adj[k][j] ) adj[i][j] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N; cin >> M;

    adj.resize(N+1, vector<bool>(N+1, false));
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a; cin >> b;
        adj[a][b] = true;
    }

    floydWarshall();

    for (int i=1; i<=N; i++) {
        int cnt = 0;
        for (int j=1; j<=N; j++) {
            if( i == j ) continue;
            if( adj[i][j] || adj[j][i] ) continue;
            cnt++;
        }
        cout << cnt << '\n';
    }
}
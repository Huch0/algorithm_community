#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, k;
vector<vector<bool>> adj;

void floydWarshall() {
    for (int k=1; k<=n; k++) {
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if( adj[i][k] && adj[k][j] ) adj[i][j] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n; cin >> k;
    adj.resize(n+1, vector<bool>(n+1, false));

    for (int i=0; i<k; i++) {
        int a, b;
        cin >> a; cin >> b;
        adj[a][b] = true;
    }

    floydWarshall();

    int s; cin >> s;

    for (int i=0; i<s; i++) {
        int a, b; cin >> a; cin >> b;
        if( adj[a][b] ) cout << -1 << '\n';
        else if( adj[b][a] ) cout << 1 << '\n';
        else cout << 0 << '\n';
    }
}
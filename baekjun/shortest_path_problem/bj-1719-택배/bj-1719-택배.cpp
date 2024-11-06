#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<vector<int>> path;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    adj.resize(n+1, vector<int>(n+1, 10000000));
    path.resize(n+1, vector<int>(n+1, 0));
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a][b] = adj[b][a] = c;
        path[a][b] = b;
        path[b][a] = a;
    }

    for (int k=1; k<=n; k++) {
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                if( i == j || i == k || j == k ) continue;
                if( adj[i][k] + adj[k][j] < adj[i][j] ) {
                    adj[i][j] = adj[i][k] + adj[k][j];
                    path[i][j] = path[i][k];
                }
            }
        }
    }

    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            if( i == j ) cout << "- ";
            else cout << path[i][j] << ' ';
        }
        cout << '\n';
    }
}
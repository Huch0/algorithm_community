#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N; cin >> N;
    vector<vector<int>> adj(N, vector<int>(N));
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) cin >> adj[i][j];

    vector<vector<int>> result(N, vector<int>(N));

    for (int i=0; i<N; i++) {
        vector<bool> visited(N);
        queue<int> q;
        q.push(i);
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int j=0; j<N; j++) {
                if( adj[cur][j] && !visited[j] ) {
                    visited[j] = true;
                    q.push(j);
                    result[i][j] = 1;
                }
            }
        }
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) cout << result[i][j] << ' ';
        cout << '\n';
    }
    
}
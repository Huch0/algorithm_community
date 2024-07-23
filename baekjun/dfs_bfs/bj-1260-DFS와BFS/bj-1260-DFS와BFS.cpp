#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<bool>> adj;

void dfs(int node, vector<bool>& visited) {
    visited[node] = true;
    cout << node+1 << " ";
    for (int i=0; i<adj.size(); i++)
        if( adj[node][i] && !visited[i] ) dfs(i, visited);
}
void bfs(int node, vector<bool>& visited) {
    queue<int> q;
    q.push(node);
    visited[node] = true;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node+1 << " ";
        for (int i=0; i<adj.size(); i++) {
            if( adj[node][i] && !visited[i] ) {
                q.push(i);
                visited[i] = true;
            }
        }
    }
}
int main() {
    int N, M, V; cin >> N >> M >> V;
    adj.assign(N, vector<bool>(N, false));
    for (int i=0; i<M; i++) {
        int a, b; cin >> a >> b;
        adj[a-1][b-1] = adj[b-1][a-1] = true;
    }

    vector<bool> visited;
    visited.assign(N, false);

    dfs(V-1, visited);
    cout << endl;

    visited.assign(N, false);
    bfs(V-1, visited);
}
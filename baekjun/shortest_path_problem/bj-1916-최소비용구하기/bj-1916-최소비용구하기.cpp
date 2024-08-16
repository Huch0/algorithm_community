#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, M;
int st, en;
vector<vector<int>> adj;
vector<int> dists;

int dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>> pq;
    pq.push({0, start});
    dists[start] = 0;

    while (!pq.empty()) {
        int curDist = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if( dists[cur] < curDist ) continue;

        for (int next = 1; next <= N; next++) {
            if (adj[cur][next] == -1) continue;

            int nextDist = curDist + adj[cur][next];
            if( nextDist < dists[next] ) {
                dists[next] = nextDist;
                pq.push({nextDist, next});
            }
        }
    }

    return dists[en];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    cin >> M;

    adj.resize(N+1, vector<int>(N+1, -1));
    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a][b] = (adj[a][b] == -1) ? c : min(adj[a][b], c);
    }

    cin >> st >> en;

    dists.resize(N+1, 2000000000);

    cout << dijkstra(st);
}
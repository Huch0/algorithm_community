#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int V, E, K;
vector<vector<pair<int, int>>> adj;
vector<int> dist;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> V >> E; cin >> K;

    adj.resize(V+1);
    dist.resize(V+1, 2000000000);

    for (int i=0; i<E; i++) {
        int u, v, w;
        cin >> u; cin >> v; cin >> w;
        adj[u].push_back({v, w});
    }

    priority_queue<pair<int, int>> pq;
    pq.push({0, K});
    dist[K] = 0;
    
    while (!pq.empty()) {
        int cost = -pq.top().first;
        int here = pq.top().second;
        pq.pop();

        if( dist[here] < cost ) continue;

        for (int i=0; i<adj[here].size(); i++) {
            int there = adj[here][i].first;
            int nextDist = cost + adj[here][i].second;

            if( dist[there] > nextDist ) {
                dist[there] = nextDist;
                pq.push({-nextDist, there});
            }
        }
    }

    for (int i=1; i<=V; i++) {
        if( dist[i] == 2000000000 ) cout << "INF\n";
        else cout << dist[i] << '\n';
    }
}
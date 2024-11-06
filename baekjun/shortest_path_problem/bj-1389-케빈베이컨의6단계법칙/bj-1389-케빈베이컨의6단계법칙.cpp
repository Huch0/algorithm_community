#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N, M;
vector<vector<int>> adj;

int kevinBaconNumber(int start) {
    vector<int> dist(N+1, -1);
    queue<int> q;
    q.push(start);
    dist[start] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int next = 1; next <= N; next++) {
            if( adj[cur][next] == 1 && dist[next] == -1 ) {
                q.push(next);
                dist[next] = dist[cur] + 1;
            }
        }
    }

    int sum = 0;
    for (int i = 1; i <= N; i++) sum += dist[i];

    return sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    adj.resize(N+1, vector<int>(N+1, 0));
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        adj[a][b] = 1;
        adj[b][a] = 1;
    }

    int minNum = 2000000000;
    int minIdx = 0;

    for (int i=1; i<=N; i++) {
        int newMin = kevinBaconNumber(i);
        if (newMin < minNum) {
            minNum = newMin;
            minIdx = i;
        }
    }

    cout << minIdx << '\n';
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int k; cin >> k;
    while (k--) {
        int v, e; cin >> v >> e;
        vector<vector<int>> graph(v+1);
        vector<int> color(v+1, 0);
        while (e--) {
            int a, b; cin >> a >> b;
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        bool flag = true;
        for (int i = 1; i <= v && flag; i++) {
            if (color[i] != 0) continue;
            queue<int> Q;
            color[i] = 1;
            Q.push(i);
            while (!Q.empty()) {
                int cur = Q.front(); Q.pop();
                for (auto nx : graph[cur]) {
                    if (color[nx] == 0) {
                        color[nx] = color[cur] % 2 + 1;
                        Q.push(nx);
                    } else if (color[nx] == color[cur]) {
                        flag = false;
                        break;
                    }
                }
            }
        }
        if (flag) cout << "YES\n";
        else cout << "NO\n";
    }
}
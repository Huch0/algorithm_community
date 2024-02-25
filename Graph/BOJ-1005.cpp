#include<bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--){
        int N, K;
        cin >> N >> K;

        int time[1002];
        for (int i = 1; i <= N; i++) {
            cin >> time[i];
        }

        vector<int> adj[1002];
        int inDeg[1002] = { 0, };
        queue<int> q;
        int result[1002];

        while (K--) {
            int X, Y;
            cin >> X >> Y;
            adj[X].push_back(Y);
            inDeg[Y]++;
        }

        int W;
        cin >> W;

        for (int i = 1; i <= N; i++) {
            if (inDeg[i] == 0) {
                q.push(i);
            }
            result[i] = time[i];
        }

        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            for (int i = 0; i < adj[cur].size(); i++) {
                int next = adj[cur][i];
                inDeg[next]--;
                result[next] = max(result[next], result[cur] + time[next]);

                if (inDeg[next] == 0) {
                    q.push(next);
                }
            }
        }

        cout << result[W] << endl;
    }

    return 0;
}

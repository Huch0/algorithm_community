#include <iostream>

using namespace std;

int t, m, n, k;
int map[51][51];
int visited[51][51];
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

void reset() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            map[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            visited[i][j] = 0;
        }
    }
}

void DFS(int y, int x) {
    visited[y][x] = 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= m || ny < 0 || ny >= n)
            continue;

        if (map[ny][nx] == 1 && visited[ny][nx] == 0) {
            DFS(ny, nx);
        }
    }
}
int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> t;

    while (t--) {
        cin >> m >> n >> k;

        reset();

        while (k--) {
            int x, y;
            cin >> x >> y;
            map[y][x] = 1;
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 1 && visited[i][j] == 0) {
                    DFS(i, j);
                    cnt++;
                }
            }
        }

        cout << cnt << endl;
    }

}



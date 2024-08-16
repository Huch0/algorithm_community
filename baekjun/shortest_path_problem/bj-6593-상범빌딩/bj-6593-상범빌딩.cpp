#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int L, R, C;
vector<vector<vector<char>>> building;
vector<vector<vector<bool>>> visited;
int dx[6] = {0, 0, 0, 0, 1, -1};
int dy[6] = {0, 0, 1, -1, 0, 0};
int dz[6] = {1, -1, 0, 0, 0, 0};

int bfs(int x, int y, int z) {
    queue<pair<pair<int, int>, int>> q;
    q.push({{x, y}, z});
    visited[z][x][y] = true;

    int dist = 0;
    while (!q.empty()) {
        int qSize = q.size();
        for (int i = 0; i < qSize; i++) {
            int curX = q.front().first.first;
            int curY = q.front().first.second;
            int curZ = q.front().second;
            q.pop();

            if( building[curZ][curX][curY] == 'E' ) return dist;

            for (int j = 0; j < 6; j++) {
                int nx = curX + dx[j];
                int ny = curY + dy[j];
                int nz = curZ + dz[j];

                if( nx < 0 || nx >= R || ny < 0 || ny >= C || nz < 0 || nz >= L ) continue;
                if( building[nz][nx][ny] == '#' || visited[nz][nx][ny] ) continue;

                q.push({{nx, ny}, nz});
                visited[nz][nx][ny] = true;
            }
        }
        dist++;
    }

    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (true) {
        cin >> L >> R >> C;
        if (L == 0 && R == 0 && C == 0) break;

        building.resize(L, vector<vector<char>>(R, vector<char>(C)));
        visited.resize(L, vector<vector<bool>>(R, vector<bool>(C, false)));
        int startX, startY, startZ;
        for (int i = 0; i < L; i++) {
            for (int j = 0; j < R; j++) {
                for (int k = 0; k < C; k++) {
                    cin >> building[i][j][k];
                    if( building[i][j][k] == 'S' ) {
                        startX = j;
                        startY = k;
                        startZ = i;
                    }
                }
            }
        }

        int result = bfs(startX, startY, startZ);
        if( result == -1 ) cout << "Trapped!\n";
        else cout << "Escaped in " << result << " minute(s).\n";

        building.clear();
        visited.clear();
    }
}
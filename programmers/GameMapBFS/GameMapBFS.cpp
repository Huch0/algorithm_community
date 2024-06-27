#include <vector>
#include <queue>
#include <climits>

using namespace std;

vector<pair<int, int>> directions{{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
int n = 0, m = 0;

int bfs(vector<vector<int>>& maps) {
    vector<vector<int>> distances(n, vector<int>(m, INT_MAX));
    queue<pair<int, int>> q;
    q.push({0, 0});
    distances[0][0] = 1;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for ( auto& d : directions ) {
            int nx = x + d.first;
            int ny = y + d.second;

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1) {
                int new_dist = distances[x][y] + 1;
                if( new_dist < distances[nx][ny] ) {
                    distances[nx][ny] = new_dist;
                    q.push({nx, ny});
                }
            }
        }
    }

    return (distances[n-1][m-1] == INT_MAX) ? -1 : distances[n-1][m-1];
}

int solution(vector<vector<int>> maps) {
    n = maps.size();
    m = maps[0].size();

    return bfs(maps);
}

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

vector<vector<int>> maps;
vector<pair<int, int>> directions{{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
int n = 0, m = 0;

void bfs() {
    vector<vector<int>> distances(n, vector<int>(m, INT_MAX));
    queue<pair<int, int>> q;
    q.push({0, 0});
    distances[0][0] = 1;

    while (!q.empty()) {
        pair<int, int> point = q.front();
        q.pop();

        for ( auto& d : directions ) {
            int nx = point.first + d.first;
            int ny = point.second + d.second;

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1) {
                int new_dist = distances[point.first][point.second] + 1;
                if( new_dist < distances[nx][ny] ) {
                    distances[nx][ny] = new_dist;
                    q.push({nx, ny});
                }
            }
        }
    }
    if( distances[n-1][m-1] != INT_MAX ) cout << distances[n-1][m-1] << endl;
    else cout << -1 << endl;

    return;
}

int main() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        vector<int> row;
        for (int j=0; j<m; j++) {
            char c; cin >> c;
            row.push_back(c-'0');
        }
        maps.push_back(row);
    }

    bfs();
    
    return 0;
}
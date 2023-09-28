#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        n = heights.size();
        m = heights[0].size();
        int start = 0, end = 1000000;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (bfs(heights, mid)) end = mid - 1;
            else start = mid + 1;
        }
        return start;
    }

    bool bfs(vector<vector<int>>& heights, int k) {
        vector<vector<bool>> vis(n, vector<bool>(m, false));
        queue<pair<int, int>> Q;
        Q.push({0, 0});
        vis[0][0] = true;

        while (!Q.empty()) {
            auto [curX, curY] = Q.front(); Q.pop();
            if (curX == n-1 && curY == m-1) return true;
            for (int dir = 0; dir < 4; dir++) {
                int nx = curX + dx[dir];
                int ny = curY + dy[dir];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m || vis[nx][ny]) continue;
                if (abs(heights[nx][ny] - heights[curX][curY]) > k) continue;

                vis[nx][ny] = true;
                Q.push({nx, ny});
            }
        }
        return false;
    }

private:
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    int n, m;
};
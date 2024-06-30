#include <iostream>
#include <queue>
using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
	int n, m, answer = 0;
	cin >> n >> m;
	vector<vector<int>> map(n, vector<int>(m));
	vector<vector<int>> visited(n, vector<int>(m, 0));

	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			char c;
			cin >> c;
			map[i][j] = c - '0';
		}
	}

	queue<pair<int, int>> q;
	q.push({0,0});
	visited[0][0] = 1;
	
	while(!q.empty()) {
		answer++;
		int qcount = q.size();
		for (int i=0; i<qcount; i++) {
			pair<int, int> cur = q.front();
			q.pop();
			int row = cur.first, col = cur.second;
			if (row == n-1 && col == m-1) {
				cout << answer;
				return 0;
			}

			for (int j=0; j<4; j++) {
				int nextrow = row + dx[j];
				int nextcol = col + dy[j];
				if (nextrow >= 0 && nextcol >= 0 && nextrow <= n-1 && nextcol <= m-1 && map[nextrow][nextcol] == 1 && visited[nextrow][nextcol] == 0) {
					visited[nextrow][nextcol] = 1;
					q.push({nextrow, nextcol});
				}
			}
		}
	}
}

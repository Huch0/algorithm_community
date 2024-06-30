#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, m, icecount = 0, answer = 0;
	cin >> n >> m;
	vector<vector<int>> map(n, vector<int>(m));
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			int k;
			cin >> k;
			map[i][j] = k;
			if (k != 0) icecount++;
		}
	}
	
	while(true) {
		int i, j, flag = 0;
		for (i=0; i<n; i++) {
			for (j=0; j<m; j++) {
				if (map[i][j] != 0) {
					flag = 1;
					break;
				}
			}
			if (flag == 1) break;
		}
		if (flag == 0) break; // 종료조건. 다 녹을때까지 분리 안된것임 
		
		int cursize = 0;
		queue<pair<int, int>> q;
		vector<vector<int>> visited(n, vector<int>(m, 0));
		q.push({i, j});
		visited[i][j] = 1;
		while(!q.empty()) {
			cursize++;
			pair<int, int> cur = q.front();
			int currow = cur.first;
			int curcol = cur.second;
			q.pop();
			
			if (currow+1 <= n-1 && map[currow+1][curcol] != 0 && visited[currow+1][curcol] == 0) {
				visited[currow+1][curcol] = 1;
				q.push({currow+1, curcol});
			}
			if (curcol+1 <= m-1 && map[currow][curcol+1] != 0 && visited[currow][curcol+1] == 0) {
				visited[currow][curcol+1] = 1;
				q.push({currow, curcol+1});
			}
			if (currow-1 >= 0 && map[currow-1][curcol] != 0 && visited[currow-1][curcol] == 0) {
				visited[currow-1][curcol] = 1;
				q.push({currow-1, curcol});
			}
			if (curcol-1 >= 0 && map[currow][curcol-1] != 0 && visited[currow][curcol-1] == 0) {
				visited[currow][curcol-1] = 1;
				q.push({currow, curcol-1});
			}
		}
		if (cursize != icecount) {
			cout << answer;
			return 0;
		}
		
		vector<vector<int>> term(map);
		for (i=0; i<n; i++) {
			for (j=0; j<m; j++) {
				if (map[i][j] != 0) {
					if (i-1 >= 0 && map[i-1][j] == 0) term[i][j]--;
					if (i+1 <= n-1 && map[i+1][j] == 0) term[i][j]--;
					if (j-1 >= 0 && map[i][j-1] == 0) term[i][j]--;
					if (j+1 <= m-1 && map[i][j+1] == 0) term[i][j]--;
					
					if (term[i][j] <= 0) {
						term[i][j] = 0;
						icecount--;
					}
				}
			}
		}
		map = term;
		answer++;
	}
	cout << "0";
}

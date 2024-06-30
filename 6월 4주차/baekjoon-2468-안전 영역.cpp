#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

int main() {
	int n, maxheight = 0, answer = 1;
	cin >> n;
	vector<vector<int>> map(n, vector<int> (n));
	set<int> possibleh;
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			int k;
			cin >> k;
			map[i][j] = k;
			possibleh.insert(k);
		}
	}

	for (int i : possibleh) {
		int safearea = 0;
		vector<vector<int>> visited(n, vector<int> (n, 0));
		while(true) {
			int j, k, flag = 0;
			for (j=0; j<n; j++) {
				for (k=0; k<n; k++) {
					if (map[j][k] > i && visited[j][k] == 0) {
						flag = 1;
						break;
					}
				}
				if (flag == 1) break;
			}
			if (flag == 0) break; // 해당 레벨에서의 탐색 끝. 물 높이 올리기
			
			queue<pair<int, int>> q;
			q.push({j, k});
			visited[j][k] = 1;
			while(!q.empty()) {
				pair<int, int> cur = q.front();
				int row = cur.first, col = cur.second;
				q.pop();
				if (row+1 <= n-1 && map[row+1][col] > i && visited[row+1][col] == 0) {
					visited[row+1][col] = 1;
					q.push({row+1, col});
				}
				if (col+1 <= n-1 && map[row][col+1] > i && visited[row][col+1] == 0) {
					visited[row][col+1] = 1;
					q.push({row, col+1});
				}
				if (row-1 >= 0 && map[row-1][col] > i && visited[row-1][col] == 0) {
					visited[row-1][col] = 1;
					q.push({row-1, col});
				}
				if (col-1 >= 0 && map[row][col-1] > i && visited[row][col-1] == 0) {
					visited[row][col-1] = 1;
					q.push({row, col-1});
				}
			}
			safearea++;
		}
		answer = max(safearea, answer);
	} 

	cout << answer;
}

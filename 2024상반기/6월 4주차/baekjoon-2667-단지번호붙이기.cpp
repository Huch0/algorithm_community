#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<vector<int>> map(n, vector<int> (n));
	vector<int> answer;
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			char c;
			cin >> c;
			map[i][j] = c - '0';
		}
	}

	while(true) {
		int i, j, flag = 0, count = 0;
		for (i=0; i<n; i++) {
			for (j=0; j<n; j++) {
				if (map[i][j] == 1) {
					flag = 1;
					break;
				}
			}
			if (flag == 1) break;
		}
		if (flag == 0) break;
		
		queue<pair<int, int>> q;
		q.push({i, j});
		map[i][j] = 0;
		
		while(!q.empty()) {
			pair<int, int> cur = q.front();
			q.pop();
			count++;
			if (cur.first+1 <= map.size()-1 && map[cur.first+1][cur.second] == 1) {
				map[cur.first+1][cur.second] = 0;
				q.push({cur.first+1, cur.second});
			}
			if (cur.second+1 <= map[0].size()-1 && map[cur.first][cur.second+1] == 1) {
				map[cur.first][cur.second+1] = 0;
				q.push({cur.first, cur.second+1});
			}
			if (cur.first-1 >= 0 && map[cur.first-1][cur.second] == 1) {
				map[cur.first-1][cur.second] = 0;
				q.push({cur.first-1, cur.second});
			}
			if (cur.second-1 >= 0 && map[cur.first][cur.second-1] == 1) {
				map[cur.first][cur.second-1] = 0;
				q.push({cur.first, cur.second-1});
			}
		}
		answer.push_back(count);
	}

	sort(answer.begin(), answer.end());
	cout << answer.size() << endl;
	for (int i=0; i<answer.size(); i++) {
		cout << answer[i] << endl;
	}
}

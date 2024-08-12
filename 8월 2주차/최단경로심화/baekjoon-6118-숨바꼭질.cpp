#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<vector<int>> a(n+1, vector<int>());
	vector<int> visited(n+1, 0);
	for (int i=0; i<m; i++) {
		int x, y; cin >> x >> y;
		a[x].push_back(y);
		a[y].push_back(x);
	}
	
	int ansnum, ansdis = -1, ansk;
	queue<int> q;
	q.push(1);
	visited[1] = 1;
	while(!q.empty()) {
		ansnum = 20001;
		ansdis++;
		int qsize = q.size();
		ansk = qsize;
		for (int i=0; i<qsize; i++) {
			int cur = q.front();
			ansnum = min(ansnum, cur);
			q.pop();
			for (int k : a[cur]) {
				if (visited[k] == 0) {
					visited[k] = 1;
					q.push(k);
				}
			}
		}
	}

	cout << ansnum << " " << ansdis << " " << ansk;
}

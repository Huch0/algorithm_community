#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
struct cmp {
	bool operator() (pair<int, int> &a, pair<int, int> &b) {
		return a > b;
	}
};

int main() {
	int n, m; cin >> n >> m;
	vector<vector<int>> a(n, vector<int>(m));
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cin >> a[i][j];
		}
	}
	for (int i=0; i<n; i++) {
		sort(a[i].begin(), a[i].end());
	}

	vector<int> indexlist(n, 1);
	priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
	int curmax = 0, answer = 1000000001;
	for (int i=0; i<n; i++) {
		pq.push({a[i][0], i});
		curmax = max(curmax, a[i][0]);
	}

	while (true) {
		pair<int, int> curmin = pq.top();
		pq.pop();
		answer = min(answer, curmax - curmin.first);
		if (indexlist[curmin.second] == m) break;
		else {
			curmax = max(curmax, a[curmin.second][indexlist[curmin.second]]);
			pq.push({a[curmin.second][indexlist[curmin.second]], curmin.second});
			indexlist[curmin.second]++;
		}
	}
	cout << answer;
}

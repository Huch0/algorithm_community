#include <iostream>
#include <vector>
#include <queue>
using namespace std;
struct cmp {
	bool operator () (pair<int, int> a, pair<int, int> b) {
		return a.second > b.second;
	}
};

int main() {
	int n, m; cin >> n >> m;
	vector<vector<pair<int, int>>> map(n+1, vector<pair<int, int>>());
	for (int i=0; i<m; i++) {
		int a, b, c; cin >> a >> b >> c;
		map[a].push_back({b,c});
	}

	int qa, qb; cin >> qa >> qb;
	vector<int> djik(n+1, -1);
	priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
	pq.push({qa, 0});

	while(!pq.empty()) {
		pair<int, int> cur = pq.top();
		pq.pop();
		if (djik[cur.first] != -1) continue;
		
		djik[cur.first] = cur.second;
		for (auto p : map[cur.first]) {
			if (djik[p.first] == -1) {
				pq.push({p.first, cur.second + p.second});
			}
		}
	}
	cout << djik[qb];
}

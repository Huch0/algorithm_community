#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

int main() {
	int n, m, answer = 0;
	cin >> n >> m;
	vector<set<int>> connect(n+1); // 0번은 무시
	vector<int> visited(n+1, 0);

	for (int i=0; i<m; i++) {
		int a, b;
		cin >> a >> b;
		connect[a].insert(b);
		connect[b].insert(a);
	}

	queue<int> q;
	q.push(1);
	visited[1] = 1;
	while(!q.empty()) {
		int cur = q.front();

		q.pop();
		for (int k : connect[cur]) {
			if (visited[k] == 0) {
				visited[k] = 1;
				q.push(k);
				answer++;
			}
		}
	}
	cout << answer;
}

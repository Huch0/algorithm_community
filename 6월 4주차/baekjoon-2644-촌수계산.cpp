#include <iostream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

int main() {
	int n, x, y, distance = 0;
	cin >> n >> x >> y;
	vector<set<int>> connect(n+1);
	vector<int> visited(n+1, 0);
	
	int c;
	cin >> c;
	for (int i=0; i<c; i++) {
		int a, b;
		cin >> a >> b;
		connect[a].insert(b);
		connect[b].insert(a);
	}
	
	queue<int> q;
	q.push(x);
	while(!q.empty()) {
		distance++;
		int childnum = q.size();
		for (int i=0; i<childnum; i++) {
			int cur = q.front();
			q.pop();
			
			for (int child : connect[cur]) {
				if (child == y) {
					cout << distance;
					return 0;
				}
				if (visited[child] == 0) {
					visited[child] = 1;
					q.push(child);
				}
			}
		}
	}
	cout << "-1";
}

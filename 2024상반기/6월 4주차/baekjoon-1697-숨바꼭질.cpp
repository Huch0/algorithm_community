#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, k, answer = 0;
	cin >> n >> k;
	queue<int> q;
	vector<int> visited(100001, 0);
	q.push(n);
	visited[n] = 1;

	while(!q.empty()) {
		int nodes = q.size();
		for (int i=0; i<nodes; i++) {
			int cur = q.front();
			q.pop();
			if (cur == k) {
				cout << answer;
				return 0;
			}

			if (cur+1 <= 100000 && visited[cur+1] == 0) {
				visited[cur+1] = 1;
				q.push(cur+1);
			}
			if (cur-1 >= 0 && visited[cur-1] == 0) {
				visited[cur-1] = 1;
				q.push(cur-1);
			}
			if (cur*2 <= 100000 && visited[cur*2] == 0) {
				visited[cur*2] = 1;
				q.push(cur*2);
			}
		}
		answer++;
	}
}

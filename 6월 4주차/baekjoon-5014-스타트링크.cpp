#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int f, s, g, u, d, answer = 0;
	cin >> f >> s >> g >> u >> d;
	vector<int> visited(f+1, 0);
	queue<int> q;
	q.push(s);
	visited[s] = 1;
	
	while(!q.empty()) {
		int childnum = q.size();
		for (int i=0; i<childnum; i++) {
			int cur = q.front();
			q.pop();
			if (cur == g) {
				cout << answer;
				return 0;
			}
			
			if (cur+u <= f && visited[cur+u] == 0) {
				visited[cur+u] = 1;
				q.push(cur+u);
			} 
			if (cur-d >= 1 && visited[cur-d] == 0) {
				visited[cur-d] = 1;
				q.push(cur-d);
			}
		}
		answer++;
	}
	cout << "use the stairs";
}

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n; cin >> n;
	vector<vector<int>> graph(n, vector<int>(n));
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			cin >> graph[i][j];
		}
	}
	
	vector<vector<int>> answer(graph);
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			queue<int> q;
			q.push(i);
			vector<int> visited(n, 0);
			
			while(!q.empty()) {
				int cur = q.front();
				q.pop();
				
				if (answer[cur][j] == 1) {
					answer[i][j] = 1;
					break;
				}
				for (int k=0; k<n; k++) {
					if (visited[k] == 0 && answer[cur][k] == 1) {
						visited[k] = 1;
						q.push(k);
					}
				}
			}
		}
	}
	
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			cout << answer[i][j] << " ";
		}
		cout << "\n";
	}
} 

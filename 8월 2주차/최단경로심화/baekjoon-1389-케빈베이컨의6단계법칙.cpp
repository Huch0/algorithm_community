#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<vector<int>> graph(n, vector<int>());
	for (int i=0; i<m; i++) {
		int x, y; cin >> x >> y;
		graph[x-1].push_back(y-1);
		graph[y-1].push_back(x-1);
	}

	vector<vector<int>> kb(n, vector<int>(n, 0));
	for (int i=0; i<n; i++) {
		for (int j=i+1; j<n; j++) {
			int itoj = -1;
			queue<int> q;
			q.push(i);
			vector<int> visited(n, 0);
			visited[i] = 1;
			
			while(!q.empty()) {
				int curqsize = q.size();
				int flag = 0;
				for (int k=0; k<curqsize; k++) {
					int cur = q.front();
					q.pop();
					if (cur == j) {
						flag = 1;
						break;
					}
					else {
						for (int l=0; l<graph[cur].size(); l++) {
							if (visited[graph[cur][l]] == 0) {
								visited[graph[cur][l]] = 1;
								q.push(graph[cur][l]);
							}
						}
					}
				}
				itoj++;
				if (flag == 1) break;
			}
			kb[i][j] = itoj;
			kb[j][i] = itoj;
		}
	}

	int answer, min = 9999999;
	for (int i=0; i<n; i++) {
		int localmin = 0;
		for (int k : kb[i]) localmin += k;
		if (min > localmin) {
			min = localmin;
			answer = i+1;
		}
	}
	cout << answer;
}

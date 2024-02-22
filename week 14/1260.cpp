#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <math.h>
#include <queue>
using namespace std;

void DFS(vector <vector <int>>& graph, int init, int nodes) {
	stack <int> dfs;
	vector <int> visited(nodes + 1, 0);
	visited[init]++;
	dfs.push(init);
	cout << init;
	while (!dfs.empty()) {
		int finished = 1;
		for (int i = 1;i < nodes + 1;i++) {
			if (graph[dfs.top()][i] == 1 && visited[i] == 0) {
				dfs.push(i);
				cout << ' ' << i;
				finished = 0;
				visited[i] = 1;
				break;
			}
		}
		if (finished) {
			dfs.pop();
			finished = 1;
		}
	}
}

void BFS(vector <vector <int>>& graph, int init, int nodes) {
	queue <int> bfs;
	vector <int> visited(nodes + 1, 0);
	visited[init]++;
	bfs.push(init);
	cout << init;
	while (!bfs.empty()) {
		for (int i = 1;i < nodes + 1;i++) {
			if (graph[bfs.front()][i] == 1 && visited[i] == 0) {
				bfs.push(i);
				cout << ' ' << i;
				visited[i] = 1;
			}
		}
		bfs.pop();
	}
}


int main() {
	int nodes;
	int edges;
	int init;
	cin >> nodes >> edges >> init;
	vector <vector<int>> graph(nodes + 1, vector <int>(nodes + 1, 0));

	int temp_x;
	int temp_y;

	while (edges--) {
		cin >> temp_x >> temp_y;
		graph[temp_x][temp_y]=1;
		graph[temp_y][temp_x]=1;
	}
	DFS(graph, init, nodes);
	cout << endl;
	BFS(graph, init, nodes);
}
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

void dijkstra(vector <vector<int>>& edges, int N,int from, vector <vector<int>> &distance)
{
	vector <int> nodes(N+1, -1);
	nodes[from] = 0;
	queue <int> bfs;
	bfs.push(from);

	while (!bfs.empty()) {
		for (int j = 1;j < N + 1;j++) {
			if (nodes[j] == -1 && edges[bfs.front()][j] == 1) {
				bfs.push(j);
				nodes[j] = nodes[bfs.front()] + 1;				
			}
		}
		bfs.pop();
	}
	//cout << from << "distance";
	for (int i = 1; i < N + 1;i++){
		//cout << nodes[i] << ' ';
		distance[from][i] = nodes[i];
	}
	//cout << endl;
}

int findSmallestIndex(const std::vector<int>& vec) {
	if (vec.empty()) {
		// Handle empty vector case
		return -1; // or throw an exception, depending on your requirements
	}

	int minIndex = 0; // Assume the first element has the minimum value initially

	for (int i = 1; i < vec.size(); ++i) {
		if (vec[i] < vec[minIndex]) {
			// Update the index of the smallest value found so far
			minIndex = i;
		}
	}

	return minIndex;
}

int main() {
	int N;
	int M;
	cin >> N >> M;
	vector <vector<int>> edges(N+1, vector <int> (N+1,0));
	int tempx;
	int tempy;
	while (M--) {
		cin >> tempx >> tempy;
		edges[tempx][tempy] = 1;
		edges[tempy][tempx] = 1;
	}
	vector <vector<int>> distance(N + 1, vector <int>(N + 1, 0));
	for (int i = 1; i < N + 1;i++) {
		dijkstra(edges, N, i, distance);
	}
	vector <int> sum(N + 1,987654321);
	for (int i = 1;i < N + 1;i++) {
		sum[i] = 0;
		for (int j = 1; j < N + 1;j++) {
			sum[i] += distance[i][j];
		}
	}
	int smallestIndex = findSmallestIndex(sum);
	cout << smallestIndex;
	cin >> N;
}
#include <bits/stdc++.h>
using namespace std;

struct edge {
	int a, b, d;
	edge(int a, int b, int d):a(a),b(b),d(d){};
	bool operator < (const edge e) const {
		return d > e.d;
	}
};

int main() {
	int n, m, a, b, c;
	cin >> n >> m;
	vector<vector<pair<int, int>>> edges(n+1);
	priority_queue<edge> pq;
	bool visited[n+1] = {0,};
	
	//input받기 
	for (int i=0; i<m; i++) {
		cin >> a >> b >> c;
		edges[a].push_back(make_pair(b, c));
		edges[b].push_back(make_pair(a, c));
	}
	
	//pq에 아무 노드나 넣어놓기
	for (auto p : edges[1]) {
		pq.push(edge(1, p.first, p.second));
	}
	edges[1].clear();
	visited[1] = 1;
	
	//prim 알고리즘
	int connection = 0;
	long long sum = 0;
	while (connection < n-1) {		
		edge top = pq.top();
		pq.pop();
		if (!visited[top.b]) {
			connection++;
			sum += top.d;
			for (auto p : edges[top.b]) {
				pq.push(edge(top.b, p.first, p.second));
			}
			edges[top.b].clear();
			visited[top.b] = 1;
		}
	}
	cout << sum;
}


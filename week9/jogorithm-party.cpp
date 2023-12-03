#include <bits/stdc++.h>
using namespace std;

void get_shortest_distance(char home, map<char, vector<char>>& graph, vector<int>& distance) {
	queue<char> bfs;
	vector<int> visited(26, 0);

	visited[home-'a'] = 1;
	bfs.push(home);

	while(!bfs.empty()) {
		for (auto c : graph[bfs.front()]) {
			if (visited[c-'a'] == 0) {
				distance[c-'a'] = distance[bfs.front()-'a'] + 3;
				bfs.push(c);
				visited[c-'a'] = 1;
			}
		}
		bfs.pop();
	}
	distance[home-'a'] = 0;
}

int main() {
	int n;
	vector<char> home(3);
	vector<vector<int>> distance (3, vector<int>(26, -2)); // a~z = 0~25
	cin >> n;
	for (int i=0; i<3; i++) {
		cin >> home[i];
	}
	
	map<char, vector<char>> graph;
	for (int i=0; i<n; i++) {
		char node, ad;
		cin >> node;
		graph[node] = vector<char>();
		while(true) {
			cin >> ad;
			if (ad == '$') break;
			graph[node].push_back(ad);
		}
	}

	for (int i=0; i<3; i++) {
		get_shortest_distance(home[i], graph, distance[i]);
	}

	char answer_place;
	int answer_time = 9999;
	for (int i=0; i<26; i++) {
		if ((distance[0][i] < 0 || distance[1][i] < 0) || distance[2][i] < 0) continue;
		int time = max(max(distance[0][i], distance[1][i]), distance[2][i]);
		if (time < answer_time) {
			answer_place = i + 'a';
			answer_time = time;
		}
	}
	if (answer_time == 9999) {
		cout << "@" << endl << "-1";
	}
	else {
		cout << answer_place << endl << answer_time;
	}
}

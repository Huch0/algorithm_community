#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
int answer = 999999999;
vector<int> team;
vector<vector<int>> stat;
void calc() {
	vector<int> oppo;
	for (int i=0; i<n; i++) {
		if (find(team.begin(), team.end(), i) == team.end()) oppo.push_back(i);
	}
	
	int a = 0, b = 0;
	for (int i=0; i<team.size(); i++) {
		for (int j=0; j<team.size(); j++) {
			if (i == j) continue;
			a += stat[team[i]][team[j]];
		}
	}
	for (int i=0; i<oppo.size(); i++) {
		for (int j=0; j<oppo.size(); j++) {
			if (i == j) continue;
			b += stat[oppo[i]][oppo[j]];
		}
	}
	answer = min(answer, abs(a-b));
}
void dfs() {
	if (team.size() == n/2) calc();
	else {
		for (int i=0; i<n; i++) {
			if (team.empty() || team.back() < i) {
				team.push_back(i);
				dfs();
				team.pop_back();
			}
		}
	}
}
int main() {
	cin >> n;
	for (int i=0; i<n; i++) {
		stat.push_back(vector<int>());
		for (int j=0; j<n; j++) {
			int k; cin >> k;
			stat[i].push_back(k);
		}
	}
	dfs();
	cout << answer;
	return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m;
vector<int> nums;
vector<int> answer;
vector<int> visited;
void dfs() {
	if (answer.size() == m) {
		for (int k : answer) cout << k << " ";
		cout << "\n";
		return;
	}

	for (int i=0; i<nums.size(); i++) {
		if (visited[i] == 1) continue;
		answer.push_back(nums[i]);
		visited[i] = 1;
		dfs();
		answer.pop_back();
		visited[i] = 0;
	}
}
int main() {
	cin >> n >> m;
	for (int i=0; i<n; i++) {
		int k; cin >> k;
		nums.push_back(k);
		visited.push_back(0);
	}
	sort(nums.begin(), nums.end());
	dfs();
}

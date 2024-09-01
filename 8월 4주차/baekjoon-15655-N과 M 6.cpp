#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m;
vector<int> nums;
vector<int> answer;
void dfs(int latestIdx) {
	if (answer.size() == m) {
		for (int k : answer) cout << k << " ";
		cout << "\n";
		return;
	}

	for (int i=latestIdx+1; i<nums.size(); i++) {
		answer.push_back(nums[i]);
		dfs(i);
		answer.pop_back();
	}
}
int main() {
	cin >> n >> m;
	for (int i=0; i<n; i++) {
		int k; cin >> k;
		nums.push_back(k);
	}
	sort(nums.begin(), nums.end());
	dfs(-1);
}

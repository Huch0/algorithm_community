#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
int n, m;
vector<int> nums;
vector<int> answer;
void dfs(int latestIndex) {
	if (answer.size() == m) {
		for (int k : answer) cout << k << " ";
		cout << "\n";
		return;
	}
	int prev = -1;
	for (int i=latestIndex; i<nums.size(); i++) {
		if (prev == nums[i]) continue;
		answer.push_back(nums[i]);
		prev = nums[i];
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
	dfs(0);
}

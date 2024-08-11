#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
int n, m;
vector<int> nums;
vector<int> answer;
void dfs() {
	if (answer.size() == m) {
		for (int k : answer) cout << k << " ";
		cout << "\n";
		return;
	}
	for (int i=0; i<nums.size(); i++) {
		answer.push_back(nums[i]);
		dfs();
		answer.pop_back();
	}
}
int main() {
	cin >> n >> m;
	set<int> myset;
	for (int i=0; i<n; i++) {
		int k; cin >> k;
		myset.insert(k);
	}
	nums = vector<int> (myset.begin(), myset.end());
	dfs();
}

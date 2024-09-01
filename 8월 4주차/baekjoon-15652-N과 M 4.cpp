#include <iostream>
#include <vector>
using namespace std;
int n, m; 
vector<int> answer;
void dfs() {
	if (answer.size() == m) {
		for (int k : answer) cout << k << " ";
		cout << "\n";
		return;
	}
	
	int i = 1;
	if (!answer.empty()) i = answer.back();
	for (; i<=n; i++) {
		answer.push_back(i);
		dfs();
		answer.pop_back();
	}
}
int main() {
	cin >> n >> m;
	dfs();
}

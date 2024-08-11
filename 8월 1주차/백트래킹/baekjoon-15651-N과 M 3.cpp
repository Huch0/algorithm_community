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
	for (int i=1; i<=n; i++) {
		answer.push_back(i);
		dfs();
		answer.pop_back();
	}
}
int main() {
	cin >> n >> m;
	dfs();
}

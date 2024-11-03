#include <iostream>
#include <vector>
using namespace std;

int n, posscase;
vector<int> answer;

void dfs() {
	if (answer.size() == n) {
		posscase++;
		return;
	}
	for (int i=0; i<n; i++) {
		int flag = 0;
		for (int j=0; j<answer.size(); j++) {
			int dist = answer.size() - j;
			if (answer[j] == i || dist == abs(i-answer[j])) {
				flag = 1;
				break;
			}
		}
		if (flag == 1) continue;
		answer.push_back(i);
		dfs();
		answer.pop_back();
	}
}

int main() {
	cin >> n;
	dfs();
	cout << posscase;
} 

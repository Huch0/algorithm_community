#include <iostream>
#include <vector>
#include <map>
using namespace std;
int minval[4];
void backtracking(int n, vector<int>& curval, vector<int>& curlist, vector<vector<int>>& info, map<int, vector<int>>& candidate) { // n번째 요소를 넣고/빼고 다음거 호출 
	for (int i=0; i<5; i++) {
		if (i==4) {
			int price = 0;
			for (int j=0; j<curlist.size(); j++) {
				price += info[curlist[j]][4];
			}
			if (candidate.count(price) == 0 || candidate[price] > curlist) candidate[price] = curlist;
			return;
		}
		else {
			if (minval[i] > curval[i]) break;
		}
	}
	if (n >= info.size()) return;
	
	// 포함하고 호출
	curlist.push_back(n);
	for (int i=0; i<4; i++) {
		curval[i] += info[n][i];
	}
	backtracking(n+1, curval, curlist, info, candidate);
	
	// 제외하고 호출
	curlist.pop_back();
	for (int i=0; i<4; i++) {
		curval[i] -= info[n][i];
	}	 
	backtracking(n+1, curval, curlist, info, candidate);
}

int main() {
	int k;
	cin >> k;
	vector<vector<int>> info(k, vector<int>(4,0));
	for (int i=0; i<4; i++) {
		cin >> minval[i];
	}
	for (int i=0; i<k; i++) {
		for (int j=0; j<5; j++) {
			cin >> info[i][j];
		}
	}
	
	map<int, vector<int>> candidate;
	vector<int> curval(4, 0);
	vector<int> curlist;
	backtracking(0, curval, curlist, info, candidate);
	
	if (candidate.size() == 0) cout << "0";
	else {
		for (auto p : candidate) {
			for (int i=0; i<p.second.size(); i++) {
				cout << p.second[i]+1 << " ";
			}
			break;
		}
	}
}
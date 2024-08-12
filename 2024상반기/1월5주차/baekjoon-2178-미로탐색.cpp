#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m, row=0, column=0, answer=0; 
	vector<vector<int>> mv;
	cin >> n >> m;
	
	for (int i=0; i<n; i++) {
		mv.push_back(vector<int>());
		string term;
		cin >> term;
		for (int j=0; j<m; j++) {
			mv[i].push_back(term[j]);
		}
	}
	
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cout << mv[i][j] << " ";
		}
		cout << endl;
	}
}
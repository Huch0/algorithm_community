#include <iostream>
#include <bits/stdc++.h>
using namespace std;

//void dfs_solution(int row, int column, int array[], int n, int m, int &answer) {
//	
//}

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
//	dfs_solution(row, column, array, n, m, answer);
//	cout << answer 
}
//더 나은 코드를 찾으려는 노력 해보기 

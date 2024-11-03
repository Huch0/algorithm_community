#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

vector<vector<int>> map(9);
vector<unordered_set<int>> row(9);
vector<unordered_set<int>> col(9);
vector<unordered_set<int>> sq(9);
int finishflag = 0;

void dfs() {
	int localfinflag = 1;
	for (int i=0; i<9; i++) {
		if (row[i].size() != 9 || col[i].size() != 9 || sq[i].size() != 9) {
			localfinflag = 0;
			break;
		}
	}
	if (localfinflag == 1) {
		cout << "fin.222222222222222222222222222222222222222222222222222222222222222";
		finishflag = 1;
		return;
	}

	for (int i=0; i<9; i++) {
		for (int j=0; j<9; j++) {
			if (map[i][j] == 0) {
				unordered_set<int> myset = {1,2,3,4,5,6,7,8,9};
				for (int k : row[i]) myset.erase(k);
				for (int k : col[j]) myset.erase(k);
				for (int k : sq[i/3*3 + j/3]) myset.erase(k);
				for (int k : myset) {
					cout << i << " " << j << "에" << k << "넣어보기" <<endl;
					map[i][j] = k;
					row[i].insert(k);
					col[j].insert(k);
					sq[i/3*3 + j/3].insert(k);
					dfs();
					if (finishflag == 1) return;
					map[i][j] = 0;
					row[i].erase(k);
					col[j].erase(k);
					sq[i/3*3 + j/3].erase(k);
				}
			}
		}
	}
}

int main() {
	for (int i=0; i<9; i++) {
		for (int j=0; j<9; j++) {
			int k; cin >> k;
			map[i].push_back(k);
			row[i].insert(k);
			col[j].insert(k);
			sq[i/3*3 + j/3].insert(k);
		}
	}

	dfs();
}

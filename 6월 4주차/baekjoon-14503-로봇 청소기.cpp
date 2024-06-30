#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, m, row, col, d, answer = 0; // 1=寒. 0=没家救等镑. -1=没家等镑 
	cin >> n >> m >> row >> col >> d;
	vector<vector<int>> map(n, vector<int> (m));
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cin >> map[i][j];
		}
	}

	while(true) {
		if (map[row][col] == 1) break;
		
		if (map[row][col] == 0) {
			map[row][col] = -1;
			answer++;
		}
		if (map[row+1][col] != 0 && map[row][col+1] != 0 && map[row-1][col] != 0 && map[row][col-1] != 0) {
			if (d == 0) row += 1;
			else if (d == 1) col -= 1;
			else if (d == 2) row -= 1;
			else col += 1;
		}
		else { // 0 3 2 1
			d = (d - 1 + 4) % 4;
			if (d == 0 && map[row-1][col] == 0) row -= 1;
			else if (d == 1 && map[row][col+1] == 0) col += 1;
			else if (d == 2 && map[row+1][col] == 0) row += 1;
			else if (d == 3 && map[row][col-1] == 0) col -= 1;
		}
	}
	cout << answer;
}

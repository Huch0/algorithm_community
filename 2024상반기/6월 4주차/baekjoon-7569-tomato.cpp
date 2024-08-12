#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef struct point {
	int row;
	int col;
	int h;
	point(int a, int b, int c) {
		row = a;
		col = b;
		h = c;
	}
} point;
int main() {
	int row, col, h; // 가로, 세로, 높이 
	cin >> col >> row >> h;
	vector<vector<vector<int>>> box(row, vector<vector<int>>(col, vector<int>(h))); // box[row][col][h];
	queue<point> q;
	int notfresh = 0;

	for (int i=0; i<h; i++) {
		for (int j=0; j<row; j++) {
			for (int k=0; k<col; k++) {
				int input;
				cin >> input;
				box[j][k][i] = input;
				
				if (input == 0) notfresh++;
				else if (input == 1) q.push(point(j, k, i));
			}
		}
	}

	int days = 0;
	while(!q.empty()) {
		if (notfresh == 0) {
			cout << days;
			return 0;
		} 
		int qcount = q.size();
		for (int i=0; i<qcount; i++) {
			point cur = q.front();
			q.pop();
			
			if (cur.row+1 <= row-1 && box[cur.row+1][cur.col][cur.h] == 0) {
				box[cur.row+1][cur.col][cur.h] = 1;
				q.push(point(cur.row+1, cur.col, cur.h));
				notfresh--;
			}
			if (cur.col+1 <= col-1 && box[cur.row][cur.col+1][cur.h] == 0) {
				box[cur.row][cur.col+1][cur.h] = 1;
				q.push(point(cur.row, cur.col+1, cur.h));
				notfresh--;
			}
			if (cur.h+1 <= h-1 && box[cur.row][cur.col][cur.h+1] == 0) {
				box[cur.row][cur.col][cur.h+1] = 1;
				q.push(point(cur.row, cur.col, cur.h+1));
				notfresh--;
			}
			if (cur.row-1 >= 0 && box[cur.row-1][cur.col][cur.h] == 0) {
				box[cur.row-1][cur.col][cur.h] = 1;
				q.push(point(cur.row-1, cur.col, cur.h));
				notfresh--;
			}
			if (cur.col-1 >= 0 && box[cur.row][cur.col-1][cur.h] == 0) {
				box[cur.row][cur.col-1][cur.h] = 1;
				q.push(point(cur.row, cur.col-1, cur.h));
				notfresh--;
			}
			if (cur.h-1 >= 0 && box[cur.row][cur.col][cur.h-1] == 0) {
				box[cur.row][cur.col][cur.h-1] = 1;
				q.push(point(cur.row, cur.col, cur.h-1));
				notfresh--;
			}
		}
		days++;
	}
	
	cout << "-1";
}

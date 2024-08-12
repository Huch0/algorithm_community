#include <bits/stdc++.h>
/*
기억할만한것
movevec을 선언해서 3차원 특정 좌표에서 다른 좌표로 이동하는 코드 빠르게 짜기 
구조체 내에서 operator 정의하기 (bool operator == (point p) {})
특정 구조체 변수에 구조체 대입하기 (start = point(a,b,c))
다른 자료형을 string으로 바꾸기 (to_string(answer))
*/
using namespace std;
vector<vector<int>> movevec = {
{1,0,0,-1,0,0},
{0,1,0,0,-1,0},
{0,0,1,0,0,-1}
};
struct point {
	int a;
	int b;
	int c;
	point(int _a, int _b, int _c) {
		a = _a;
		b = _b;
		c = _c;
	}
	bool operator == (point p) {
		return (a == p.a && b == p.b && c == p.c);
	}
};
int main() {
	vector<string> answer;
	while (true) {
		int l, r, c; cin >> l >> r >> c;
		if (l==0 && r==0 && c==0) break;
		
		vector<vector<vector<int>>> graph(l, vector<vector<int>>(r, vector<int>(c, 1)));
		point start(0,0,0), end(0,0,0);
		for (int i=0; i<l; i++) {
			for (int j=0; j<r; j++) {
				for (int k=0; k<c; k++) {
					char input; cin >> input;
					if (input == '.') graph[i][j][k] = 0;
					else if (input == 'S') start = point(i, j, k);
					else if (input == 'E') end = point(i, j, k);
				}
			}
		}
		
		queue<point> q;
		q.push(start);
		int mintime = 0;
		int flag = 0;
		while (!q.empty() && flag == 0) {
			mintime++;
			int qsize = q.size();
			for (int i=0; i<qsize; i++) {
				point cur = q.front();
				q.pop();
				
				for (int j=0; j<6; j++) {
					int nextl = cur.a + movevec[0][j];
					if (nextl < 0 || nextl >= l) continue;
					int nextr = cur.b + movevec[1][j];
					if (nextr < 0 || nextr >= r) continue;
					int nextc = cur.c + movevec[2][j];
					if (nextc < 0 || nextc >= c) continue;
					
					if (point(nextl, nextr, nextc) == end) {
						flag = 1;
						break;
					}
					if (graph[nextl][nextr][nextc] == 0) {
						graph[nextl][nextr][nextc] = 1;
						q.emplace(nextl, nextr, nextc);
					}
				}
				if (flag == 1) break;
			}
		}
		if (flag == 1) answer.push_back("Escaped in " + to_string(mintime) + " minute(s).");
		else answer.push_back("Trapped!");
	}

	for (int i=0; i<answer.size(); i++) {
		cout << answer[i];
		if (i != answer.size()-1) cout << "\n";
	}
}


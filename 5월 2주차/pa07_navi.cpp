#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <queue>
#define MAX 9999999
using namespace std;
typedef struct point {
	int x;
	int y;
	point(int _x, int _y) : x(_x), y(_y) {}
	bool operator == (const point p) {
		return (x==p.x && y==p.y);
	}
	int getd(point p) {
		return sqrt(pow(x-p.x, 2) + pow(y-p.y, 2));
	}
} point;
typedef struct cell{
	point p;
	int gx;
	int hx;
	int fx;
	cell(point _p, int _gx, int _hx) : p(_p), gx(_gx), hx(_hx) {
		fx = _gx + _hx;
	}
	bool operator < (const cell c) const {
		return fx > c.fx;
	}
} cell;
int main() {
	int m, n, z, a, b, c, f;
	char d, e;
	cin >> m >> n >> z;
	vector<vector<int> > map(m, vector<int>(n, MAX));
	for (int i=0; i<z; i++) {
		cin >> a >> b >> c;
		map[b][c] = 0; // 
	}
	
	cin >> d >> b >> c;
	point start(b,c);
	cin >> d >> b >> c;
	point end(b,c);
	cell startcell(start, 0, start.getd(end));
	
	cin >> d >> e >> f;
	for (int i=0; i<f; i++) {
		cin >> z >> a >> b >> c; // (z,a) (b,c)
		
		if (z > b) swap(z,b);
		if (a > c) swap(a,c);
		for (int x=z; x<=b; x++) {
			for (int y=a; y<=c; y++) {
				map[x][y] = 0;
			}
		}
	}

	priority_queue<cell> pq;
	pq.push(startcell);
	cell current = pq.top();
	while (true) {
		current = pq.top();
		pq.pop();
		if (current.p == end) break;

		if (current.p.x-1 >= 0) {
			point downp(current.p.x-1, current.p.y);
			cell down(downp, current.gx+3, downp.getd(end));
			if (down.fx < map[current.p.x-1][current.p.y]) {
				map[current.p.x-1][current.p.y] = down.fx;
				pq.push(down);
			}
		}
		if (current.p.x+1 < m) {
			point upp(current.p.x+1, current.p.y);
			cell up(upp, current.gx+3, upp.getd(end));
			if (up.fx < map[current.p.x+1][current.p.y]) {
				map[current.p.x+1][current.p.y] = up.fx;
				pq.push(up);
			}
		}
		if (current.p.y-1 >= 0) {
			point leftp(current.p.x, current.p.y-1);
			cell left(leftp, current.gx+3, leftp.getd(end));
			if (left.fx < map[current.p.x][current.p.y-1]) {
				map[current.p.x][current.p.y-1] = left.fx;
				pq.push(left);
			}
		}
		if (current.p.y+1 < n) {
			point rightp(current.p.x, current.p.y+1);
			cell right(rightp, current.gx+3, rightp.getd(end));
			if (right.fx < map[current.p.x][current.p.y+1]) {
				map[current.p.x][current.p.y+1] = right.fx;
				pq.push(right);
			}
		}
	}
	cout << current.fx;
	return 0;
}

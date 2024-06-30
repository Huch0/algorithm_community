#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef struct point {
	int x;
	int y;
	point(int _x, int _y) {
		x = _x;
		y = _y;
	}
} point;
int distance(point a, point b) {
	return abs(a.x-b.x) + abs(a.y-b.y);
}
int main() {
	int t;
	cin >> t;
	vector<int> answer(t, 0);
	for (int casecount=0; casecount<t; casecount++) {
		int n;
		cin >> n;
		point home(0,0), target(0,0);
		vector<point> shop(n, point(0,0));
		vector<int> visitedshop(n, 0);
		cin >> home.x >> home.y;
		for (int i=0; i<n; i++) {
			cin >> shop[i].x >> shop[i].y;
		}
		cin >> target.x >> target.y;
		
		queue<point> q;
		q.push(home);
		while(!q.empty()) {
			point cur = q.front();
			q.pop();
			if (distance(cur, target) <= 1000) {
				answer[casecount] = 1;
				break;
			}
			
			for (int i=0; i<n; i++) {
				if (distance(cur, shop[i]) <= 1000 && visitedshop[i] == 0) {
					visitedshop[i] = 1;
					q.push(shop[i]);
				}
			}
		}
	}
	
	for (int i=0; i<answer.size(); i++) {
		if (answer[i] == 1) cout << "happy\n";
		else cout << "sad\n";
	}
}

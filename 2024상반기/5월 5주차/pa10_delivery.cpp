#include <iostream>
#include <vector>
#include <map>
using namespace std;
typedef struct point {
	int index;
	int x;
	int y;
	point(int _index, int _x, int _y):index(_index), x(_x), y(_y) {}
	int distance(point &p) {
		return abs(x-p.x) + abs(y-p.y);
	}
	bool operator < (const point& p) const {
		return index < p.index;
	}
} point;
int n;
point current(0, 500,500);
vector<point> store;
vector<point> home;
pair<int, vector<point>> term;
pair<int, vector<point>> answer;

void dfs() {
//	cout << term.first << " / ";
//	for (int i=0; i<term.second.size(); i++) {
//		cout << term.second[i].index << " ";
//	}
//	cout << endl;
	
	if (term.second.size() == 2*n) {
		if (term.first < answer.first || (term.first == answer.first && term.second < answer.second)) answer = term;
		return;
	}
	if (term.first >= answer.first) return; 
	if (store.size()+2 < home.size()) return; 
	
	int d;
	point cur = current;
	for (int i=0; i<store.size(); i++) {
		d = current.distance(store[i]);
		term.first += d;
		term.second.push_back(store[i]);
		current = store[i];
		store.erase(store.begin() + i);
		dfs();
		term.first -= d;
		current = cur;
		store.insert(store.begin() + i, term.second.back());
		term.second.pop_back();
	}
	for (int i=0; i<home.size(); i++) {
		int homeid = home[i].index, flag = 0;
		for (int j=0; j<store.size(); j++) {
			if (-homeid == store[j].index) flag = 1;
		}
		if (flag == 1) continue;
		
		d = current.distance(home[i]);
		term.first += d;
		term.second.push_back(home[i]);
		current = home[i];
		home.erase(home.begin() + i);
		dfs();
		term.first -= d;
		current = cur;
		home.insert(home.begin() + i, term.second.back());
		term.second.pop_back();
	}
}

int main() {
	int x, y;
	cin >> n;

	for (int i=0; i<n; i++) {
		cin >> x >> y;
		store.push_back(point(i+1, x, y));
		cin >> x >> y;
		home.push_back(point(-(i+1), x, y));
	}
	
	answer.first = 999999999; 
	dfs();
	
	for (int i=0; i<answer.second.size(); i++) {
		cout << answer.second[i].index << " ";
	}
}


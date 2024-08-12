#include <iostream>
#include <queue>
using namespace std;
struct student {
	int a;
	int b;
	int c;
	student(int _a, int _b, int _c) {
		a = _a;
		b = _b;
		c = _c;
	}
};
struct cmp {
	bool operator() (student a, student b) {
		return a.b > b.b;
	}
};
int main() {
	priority_queue<student, vector<student>, cmp> pq;
	for (int i=0; i<10; i++) {
		pq.emplace(i,-i,i);
	}
	for (int i=0; i<10; i++) {
		cout << pq.top().b << " ";
		pq.pop();
	}
}

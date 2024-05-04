#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAXVAL 999999999
using namespace std;
void calculate_time(vector<vector<pair<int, int> > > connection, vector<int> &time, int start) {
	queue<int> q;
	int cur;
	q.push(start);
	time[start] = 0;
	
	while (!q.empty()) {
		cur = q.front();
		q.pop();
		for (int i=0; i<connection[cur].size(); i++) {
			int next = connection[cur][i].first;
			int d = connection[cur][i].second;
			if (d + time[cur] < time[next]) {
				time[next] = d + time[cur];
				q.push(next);
			}
		}
	}
}
int main() {
	int N, c1, c2, a, b, c;
	cin >> N >> c1 >> c2;
	vector<vector<pair<int, int> > > connection(N+1);
	vector<int> time(N+1, MAXVAL);
	for (int i=0; i<N-1; i++) {
		cin >> a >> b >> c;
		connection[a].push_back(make_pair(b, c));
		connection[b].push_back(make_pair(a, c));
	}

	calculate_time(connection, time, c1);
	calculate_time(connection, time, c2);
	
	vector<pair<int, int> > tosort;
	for (int i=1; i<time.size(); i++) {
		if (time[i] == 0) continue;
		tosort.push_back(make_pair(time[i], i));
	}
	sort(tosort.begin(), tosort.end());
	for (int i=0; i<tosort.size(); i++) {
		cout << tosort[i].second << endl;
	}
}

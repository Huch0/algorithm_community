#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<vector<int>> a(n, vector<int>(n));
	vector<vector<long long>> v(n, vector<long long>(n, 0));
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			cin >> a[i][j];
		}
	}
	v[0][0] = 1;
	
	set<pair<int, int>> myset;
	myset.insert({0,0});
	while(!myset.empty()) {
		pair<int, int> cur = *(myset.begin());
		myset.erase(myset.begin());
		int curnum = a[cur.first][cur.second];
		if (curnum == 0) continue;
		long long curv = v[cur.first][cur.second];
		
		if (curnum + cur.first < n) {
			myset.insert({curnum + cur.first, cur.second});
			v[curnum + cur.first][cur.second] += curv;
		}
		if (curnum + cur.second < n) {
			myset.insert({cur.first, curnum + cur.second});
			v[cur.first][curnum + cur.second] += curv;
		} 
	}
	cout << v[n-1][n-1];
}

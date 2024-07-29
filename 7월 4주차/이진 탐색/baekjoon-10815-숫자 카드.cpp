#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	unordered_set<int> a;
	int n; cin >> n;
	for (int i=0; i<n; i++) {
		int k; cin >> k;
		a.insert(k);
	}
	int m; cin >> m;
	vector<int> b(m);
	for (int i=0; i<m; i++) cin >> b[i];
	for (int i=0; i<m; i++) {
		if (a.find(b[i]) == a.end()) cout << "0 ";
		else cout << "1 ";
	}
}

//연습을 위한 이진탐색 구현
/*
int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	int m; cin >> m;
	vector<int> b(m);
	for (int i=0; i<m; i++) cin >> b[i];
	
	sort(a.begin(), a.end());
	for (int i=0; i<m; i++) {
		int target = b[i];
		int start = 0, end = n-1, flag = 0;
		while(start<=end) {
			if (a[(start+end)/2] < target) start = (start+end)/2+1;
			else if (a[(start+end)/2] > target) end = (start+end)/2-1;
			else {
				flag = 1;
				break;
			}
		}
		cout << flag << " ";
	}
}
*/

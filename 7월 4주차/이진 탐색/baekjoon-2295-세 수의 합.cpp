#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;
/*
n^3º¸´Ù n^2 + n^2ÀÌ ³´´Ù. 
*/
int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	sort(a.begin(), a.end());
	unordered_set<int> twosum;
	for (int i=0; i<n; i++) {
		for (int j=i; j<n; j++) {
			twosum.insert(a[i] + a[j]);
		}
	}

	for (int i=n-1; i>0; i--) {
		for (int j=0; j<i; j++) {
			if (twosum.find(a[i] - a[j]) != twosum.end()) {
				cout << a[i];
				return 0;
			}
		}
	}
	return 0;
}

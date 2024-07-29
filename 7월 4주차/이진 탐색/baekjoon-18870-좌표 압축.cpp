#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n);
	map<int, int> zip;
	for (int i=0; i<n; i++) cin >> a[i];

	vector<int> b(a);
	sort(b.begin(), b.end());
	auto start = b.begin(), end = b.begin();
	int zipnum = 0;
	while(end != b.end()) {
		end = upper_bound(b.begin(), b.end(), *start);
		zip[*start] = zipnum++;
		start = end;
	}
	for (int i=0; i<n; i++) {
		cout << zip[a[i]] << " ";
	}
}

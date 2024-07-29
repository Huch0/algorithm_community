#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// sol1 (처음풀이)
// N개 조각으로 나눌 수 있는 길이의 범위가 있는데, 그중 가장 큰 것을 이진탐색으로 찾는 문제. / 어떻게 가장 큰 것을 찾을까 ? 
/*
int main() {
	long long n; cin >> n;
	long long m; cin >> m;
	vector<long long> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	long long sum = 0;
	for (int i=0; i<n; i++) sum += a[i];

	long long start = 1, end = sum/m;
	while(start<end) {
		long long curlen = (start+end)/2;
		long long cur = 0;
		for (int i=0; i<n; i++) {
			cur += a[i]/curlen;
		}

		if (cur < m) end = (start+end)/2 - 1;
		else {
			curlen++;
			cur = 0;
			for (int i=0; i<n; i++) {
				cur += a[i]/curlen;
			}
			if (cur < m) {
				cout << curlen-1;
				return 0;
			}
			else start = (start+end)/2 + 1;
		}
	}
	cout << start;
	return 0;
}
*/

//sol2
int main() {
	long long n; cin >> n;
	long long m; cin >> m;
	vector<long long> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	long long sum = 0;
	for (int i=0; i<n; i++) sum += a[i];

	long long start = 1, end = sum/m;
	while(start<=end) {
		long long curlen = (start+end)/2;
		long long cur = 0;
		for (int i=0; i<n; i++) {
			cur += a[i]/curlen;
		}

		if (cur < m) end = (start+end)/2 - 1;
		else start = (start+end)/2 + 1;
	}
	cout << end;
	return 0;
}

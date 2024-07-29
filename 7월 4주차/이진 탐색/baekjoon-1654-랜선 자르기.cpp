#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// sol1 (ó��Ǯ��)
// N�� �������� ���� �� �ִ� ������ ������ �ִµ�, ���� ���� ū ���� ����Ž������ ã�� ����. / ��� ���� ū ���� ã���� ? 
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

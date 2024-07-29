#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	if (m==0) {
		cout << 0;
		return 0;
	}
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	sort(a.begin(), a.end());

	int answer = 2000000001;
	int start = 0, end = 1;
	int dif = a[1] - a[0];
	while (start < n-1) {
		if (dif < m || start == end) {
			dif -= a[end];
			end++;
			if (end == n) break;
			dif += a[end];
		}
		else {
			answer = min(answer, dif);
			dif += a[start];
			start++;
			dif -= a[start];
		}
	}

	cout << answer;
}

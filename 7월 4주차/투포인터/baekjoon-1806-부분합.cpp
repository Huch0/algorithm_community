#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, s; cin >> n >> s;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	int sum = 0, minlen = 100001;
	int start = 0, end = 0;
	while (end <= n) {
		if (sum < s || start == end) {
			if (end == n) break;
			sum += a[end];
			end++;
		}
		else {
			minlen = min(minlen, end - start);
			sum -= a[start];
			start++;
		}
	}
	
	if (minlen == 100001) cout << 0;
	else cout << minlen;
}

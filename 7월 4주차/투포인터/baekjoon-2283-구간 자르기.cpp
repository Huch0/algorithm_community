#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, k; cin >> n >> k;
	vector<int> a(1000000, 0);
	for (int i=0; i<n; i++) {
		int x, y; cin >> x >> y;
		for (int j=x; j<y; j++) {
			a[j]++;
		}
	}
	
	int start = 0, end = 0;
	int cursum = 0;
	while (end <= a.size()) {
		if (cursum == k) {
			cout << start << " " << end;
			return 0;
		}
		else if (cursum < k || start == end) {
			cursum += a[end];
			end++;
		}
		else {
			cursum -= a[start];
			start++;
		}
	}
	cout << "0 0";
}

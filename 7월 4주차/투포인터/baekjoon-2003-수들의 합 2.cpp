#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, target; cin >> n >> target;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	int answer = 0;
	int start = 0, end = 1;
	int cursum = a[0];
	while (end<=n) {
		if (cursum < target || start == end) {
			if (end == n) break;
			cursum += a[end];
			end++;
		}
		else if (cursum > target) {
			cursum -= a[start];
			start++;
		}
		else {
			answer++;
			cursum -= a[start];
			start++;
		}
	}
	
	cout << answer;
}

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	vector<int> dp(n, 1);
	int answer = 0;
	for (int i=0; i<n; i++) {
		int m = 0;
		for (int j=i-1; j>=0; j--) {
			if (a[j] < a[i]) m = max(m, dp[j]);
		}
		dp[i] = m+1;
		answer = max(answer, dp[i]);
	}

	cout << answer;
}

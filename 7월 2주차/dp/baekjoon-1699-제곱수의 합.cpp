#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
vector<int> dnum;
int myfunc(vector<int> &dp, int n) {
	if (dp[n] != -1) return dp[n];
	int i;
	for (i = dnum.size()-1; i>=0; i--) {
		if (dnum[i] <= n) break;
	}

	int minsum = 100001;
	for (; i>=1; i--) {
		minsum = min(minsum, myfunc(dp, dnum[i]) + myfunc(dp, n - dnum[i]));
	}
	dp[n] = minsum;
	return minsum;
}
int main() {
	for (int i=0; i*i<=100000; i++) dnum.push_back(i*i);
	int n; cin >> n;
	vector<int> dp(n+1, -1);
	for (int i=0; i*i<=n; i++) {
		dp[i*i] = 1;
	}
	cout << myfunc(dp, n);
}

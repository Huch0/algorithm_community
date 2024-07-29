#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n+1, 1);
	a[0] = 0; a[1] = 0;
	for (int i=2; i<=sqrt(n); i++) {
		if (a[i] == 0) continue;
		for (int j=i+i; j<=n; j+=i) {
			a[j] = 0;
		}
	}
	vector<int> prime;
	for (int i=0; i<=n; i++) {
		if (a[i] == 1) prime.push_back(i);
	}
	if (prime.size() == 0) {
		cout << 0;
		return 0;
	}

	int answer = 0;
	int start = 0, end = 1, sum = prime[0];
	while (end <= prime.size()) {
		if (sum < n || start == end) {
			if (end == prime.size()) break;
			sum += prime[end];
			end++;
		}
		else if (sum > n) {
			sum -= prime[start];
			start++;
		}
		else {
			answer++;
			sum -= prime[start];
			start++;
		}
	}

	cout << answer;
}

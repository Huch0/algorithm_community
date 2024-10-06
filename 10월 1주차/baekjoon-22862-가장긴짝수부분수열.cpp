#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, k; cin >> n >> k;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	int answer = 0;
	int curodd = 0;
	int start = 0, end = 0;
	while (end <= n) {
		if (curodd <= k || start == end) {
			answer = max(answer, end - start - curodd);
			if (end == n) break;
			
			if (a[end]%2 == 1) curodd++;
			end++;
		}
		else {
			if (a[start]%2 == 1) curodd--;
			start++;
		}
	}
	
	cout << answer;
}

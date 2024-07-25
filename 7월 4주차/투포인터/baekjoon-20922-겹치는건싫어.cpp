#include <iostream>
#include <vector>
using namespace std;
int count[100000000];
int main() {
	int n, k; cin >> n >> k;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	int answer = 1;
	int start = 0, end = 1;
	count[a[start]]++;
	while (end < n) {
		if (count[a[end]] + 1 <= k) {
			count[a[end]]++;
			end++;
			answer = max(answer, end - start);
		}
		else {
			while(true) {
				count[a[start]]--;
				start++;
				if (a[start-1] == a[end]) break;
			}
		}
	}
	cout << answer;
}

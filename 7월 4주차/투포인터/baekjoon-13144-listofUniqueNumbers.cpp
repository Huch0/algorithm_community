#include <iostream>
#include <vector>
using namespace std;

int flag[100001];

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	int start = 0, end = 0;
	long long answer = 0;
	while (start < n) {
		if (flag[a[end]] == 1 || end == n) {
			answer += (end-start);
			flag[a[start]]--;
			start++;
		}
		else {
			flag[a[end]]++;
			end++;
		}
	}
	cout << answer;
}

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	int answer = a[0];
	for (int i=1; i<n; i++) {
		if (a[i-1] > 0) a[i] += a[i-1];
		answer = max(answer, a[i]);
	}
	cout << answer;
}

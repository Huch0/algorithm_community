#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	sort(a.begin(), a.end());
	int answer = 0;
	for (int i=0; i<n; i++) {
		for (int j=0; j<=i; j++) answer += a[j];
	}
	cout << answer;
}

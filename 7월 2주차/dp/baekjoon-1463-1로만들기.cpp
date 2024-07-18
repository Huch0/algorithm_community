#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, answer = 0;
	cin >> n;
	vector<int> a(n+1, 0);
	
	for (int i=2; i<=n; i++) {
		int k = 999999999;
		if (i%3 == 0) k = min(k, a[i/3] + 1);
		if (i%2 == 0) k = min(k, a[i/2] + 1);
		k = min(k, a[i-1] + 1);
		a[i] = k;
	}
	cout << a[n];
} 

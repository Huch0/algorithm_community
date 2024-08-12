#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	vector<int> m(n, 0);
	m[0] = a[0];
	m[1] = a[0] + a[1];
	m[2] = a[2] + max(a[0], a[1]);
	for (int i=3; i<n; i++) {
		m[i] = a[i] + max(m[i-2], m[i-3] + a[i-1]);
	}
	cout << m[n-1];
}

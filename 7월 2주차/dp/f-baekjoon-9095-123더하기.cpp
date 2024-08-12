#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> a(11, 0);
	a[1] = 1;
	a[2] = 2;
	a[3] = 4;
	for (int i=4; i<=10; i++) {
		a[i] = a[i-3] + a[i-2] + a[i-1];
	}
	
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		int n; cin >> n;
		cout << a[n] << "\n";
	}
}

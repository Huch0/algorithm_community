#include <iostream>
using namespace std;

int main() {
	int a[46] = {0, };
	a[0] = 0;
	a[1] = 1;
	for (int i=2; i<46; i++) {
		a[i] = a[i-2] + a[i-1];
	}
	
	int k;
	cin >> k;
	cout << a[k];
}

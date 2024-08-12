#include <iostream>
using namespace std;

int main() {
	int n, x, curnum=0, maxnum=0, cnt;
	cin >> n >> x;
	int array[n];
	for (int i=0; i<n; i++) {
		cin >> array[i];
	}
	
	for (int i=0; i<x; i++) {
		curnum += array[i];
	}
	maxnum = curnum;
	cnt = 1;
	for (int i=0; i<n-x; i++) {
		curnum -= array[i];
		curnum += array[i+x];
		if (curnum > maxnum) {
			maxnum = curnum;
			cnt = 1;
		}
		else if (curnum == maxnum) cnt++;
	}
	
	if (maxnum != 0) {
		cout << maxnum << endl << cnt;
	}
	else cout << "SAD";
	
}

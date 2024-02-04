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
	maxnum = curnum; // 초기화 
	cnt = 1;
	for (int i=0; i<n-x; i++) { // n=5 x=2이면 01 12 23 34 이렇게 4개에 대해서 고려해줘야 
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

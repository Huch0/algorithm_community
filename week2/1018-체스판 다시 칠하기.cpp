#include <iostream>
using namespace std;

int main() {
	int m, n, min = 99, count;
	cin >> m >> n;
	char array[m][n];
	for (int i=0; i<m; i++) {
		for (int j=0; j<n; j++) {
			cin >> array[i][j];
		}
	}
	
	for (int i=0; i<m-7; i++) {
		for (int j=0; j<n-7; j++) {
			count = 0;
			for (int k=i; k<i+8; k++) {
				for (int l=j; l<j+8; l++) { 
					if ((k+l) % 2 == 0) {
						if (array[k][l] == 'B') count++;
					} else {
						if (array[k][l] == 'W') count++;
					}
				}
			}
			if (min > count) min = count;
			count = 0;
			
			for (int k=i; k<i+8; k++) {
				for (int l=j; l<j+8; l++) { 
					if ((k+l) % 2 == 0) {
						if (array[k][l] == 'W') count++;
					} else {
						if (array[k][l] == 'B') count++;
					}
				}
			}
			if (min > count) min = count;
		}	
	}
	cout << min;
}

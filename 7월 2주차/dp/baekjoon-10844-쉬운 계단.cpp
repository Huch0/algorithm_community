#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<vector<int>> a(n+1, vector<int>(10, 0));
	for (int i=0; i<10; i++) a[1][i] = 1;
	for (int i=2; i<=n; i++) {
		for (int j=0; j<10; j++) {
			if (j-1 >= 0) a[i][j] = (a[i][j] + a[i-1][j-1])%1000000000;
			if (j+1 <= 9) a[i][j] = (a[i][j] + a[i-1][j+1])%1000000000;
		}
	}

	int answer = 0;
	for (int i=1; i<=9; i++) {
		answer = (answer + a[n][i])%1000000000;
	}
	cout << answer;
}

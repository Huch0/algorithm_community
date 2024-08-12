#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<vector<int>> a(n, vector<int>(m));
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) cin >> a[i][j];
	}
	
	for (int i=1; i<m; i++) {
		a[0][i] += a[0][i-1];
	}
	for (int i=1; i<n; i++) {
		for (int j=0; j<m; j++) {
			if (j==0) a[i][j] += a[i-1][j];
			else a[i][j] += max(a[i-1][j], a[i][j-1]);
		}
	}
	cout << a[n-1][m-1];
} 

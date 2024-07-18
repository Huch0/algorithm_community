#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<vector<int>> a(n, vector<int>(10, 1));

	for (int i=1; i<n; i++) {
		for (int j=0; j<10; j++) {
			int sum = 0;
			for (int k=j; k<10; k++) {
				sum = (sum + a[i-1][k])%10007;
			}
			a[i][j] = sum;
		}
	}

	int answer = 0;
	for (int i=0; i<10; i++) answer = (answer + a[n-1][i])%10007;
	cout << answer;
}

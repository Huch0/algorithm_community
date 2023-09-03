#include <iostream>
using namespace std;
int main() {
	int n, m;
	int answer=0;
	
	cin >> n >> m;
	int array[n];
	for (int i=0; i<n; i++) {
		cin >> array[i];
	}
	
	for (int i=0; i<n-2; i++) {
		for (int j=i+1; j<n-1; j++) {
			for (int k=j+1; k<n; k++) {
				int sum = array[i] + array[j] + array[k];
				if (sum > answer && sum <= m) {
					answer = array[i] + array[j] + array[k];
				}
			}
		}
	}
	
	cout << answer;
}

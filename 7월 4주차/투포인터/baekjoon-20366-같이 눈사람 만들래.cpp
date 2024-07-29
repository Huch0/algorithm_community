#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	sort(a.begin(), a.end());
	
	int answer = 1000000001;
	for (int i=0; i<n; i++) {
		for (int j=i+3; j<n; j++) {
			int height = a[i] + a[j];
			int small = i+1, big = j-1;
			while (small != big) {
				answer = min(answer, abs(height - (a[small] + a[big])));
				if (answer == 0) {
					cout << 0;
					return 0;
				}
				else if (a[small] + a[big] < height) small++;
				else big--;
			}
		}
	}
	cout << answer;
}

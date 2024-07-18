#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n; cin >> n;
	int answer = 0;
	vector<int> sq;
	
	for (int k=1; k*k<=100000; k++) sq.push_back(k*k);
	for (int i=sq.size()-1; i>=0; i--) {
		while (sq[i] <= n) {
			answer++;
			n -= sq[i];
		}
	}
	cout << answer;
}

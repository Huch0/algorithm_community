#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int pascal(int N, int k) {
	if (k == 0) {
		return 1;
	}
	if (k == 1) {
		return N;
	}
	if (N == k) {
		return 1;
	}
	if (N == k + 1) {
		return N;
	}
	return pascal(N - 1, k) + pascal(N - 1, k - 1);
}

int main() {
	int N;
	int k;

	cin >> N;
	cin >> k;
	
	if (N - k < k) {
		k = N - k;
	}

	cout << pascal(N,k);
}
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	
	double score[n];
	for (int i=0; i<n; i++) {
		cin >> score[i];
	}
	
	sort(score, score+n);
	cout << score[n-k];
}

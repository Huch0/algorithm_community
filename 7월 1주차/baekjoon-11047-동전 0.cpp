#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	vector<int> price(n);
	for (int i=0; i<n; i++) cin >> price[i];
	
	int answer = 0, index = n-1;
	while(k > 0) {
		if (price[index] <= k) {
			k -= price[index];
			answer++;
		}
		else index--;
	}
	cout << answer;
}

//sol2
int main() {
	int n, k;
	cin >> n >> k;
	vector<int> price(n);
	for (int i=0; i<n; i++) cin >> price[i];
	
	int answer = 0;
	for (int i=n-1; i>=0 && k>0; i--) {
		int div = k/price[i];
		answer += div;
		k -= div * price[i];
	}
	cout << answer;
}
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	long long n, m;
	cin >> n >> m;
	priority_queue<long long, vector<long long>, greater<long long>> pq;
	for (int i=0; i<n; i++) {
		int k;
		cin >> k;
		pq.push(k);
	}
	
	for (int i=0; i<m; i++) {
		long long a, b;
		a = pq.top();
		pq.pop();
		b = pq.top();
		pq.pop();
		pq.push(a+b);
		pq.push(a+b);
	}
	
	long long answer = 0;
	while(!pq.empty()) {
		answer += pq.top();
		pq.pop();
	}
	cout << answer;
}

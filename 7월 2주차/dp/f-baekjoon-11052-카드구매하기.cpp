#include <iostream>
#include <vector>
using namespace std;
/*
knapsack problem을 다시 생각해보자
물건을 자를 수 있다면 단순히 p/w가 큰 순서대로 넣으면 되겠지만, 0-1 knapsack의 경우 p/w가 큰것부터 넣는 단순한 접근으로 해결할 수 없다.
이 문제도 마찬가지로, 단순히 카드 1장당 가치가 큰 카드팩부터 사는 것으로는 해결하지 못한다.

동적 계획법 : Bottom-up approach, 작은 문제들의 해를 저장해서 이를 이용해 큰 문제를 품 (메모이제이션)
작은 문제들과 큰 문제 사이의 점화식을 세워야 한다 
*/

int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];

	vector<int> dp(n+1, 0);
	for (int i=1; i<=n; i++) {
		for (int j=0; j<i; j++) {
			dp[i] = max(dp[i], dp[j] + a[i-j-1]);
		}
	}
	cout << dp[n];
}

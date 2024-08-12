#include <iostream>
#include <vector>
using namespace std;
/*
knapsack problem�� �ٽ� �����غ���
������ �ڸ� �� �ִٸ� �ܼ��� p/w�� ū ������� ������ �ǰ�����, 0-1 knapsack�� ��� p/w�� ū�ͺ��� �ִ� �ܼ��� �������� �ذ��� �� ����.
�� ������ ����������, �ܼ��� ī�� 1��� ��ġ�� ū ī���Ѻ��� ��� �����δ� �ذ����� ���Ѵ�.

���� ��ȹ�� : Bottom-up approach, ���� �������� �ظ� �����ؼ� �̸� �̿��� ū ������ ǰ (�޸������̼�)
���� ������� ū ���� ������ ��ȭ���� ������ �Ѵ� 
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

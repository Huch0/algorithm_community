#include <iostream>
using namespace std;

int main() {
	int n, divsum;
	cin >> n; // 이 n의 가장작은 생성자를 구해야 함

	for (int i=1; i<=n; i++) {
		divsum = i;
		int term = i;
		while (term) {
			divsum += term%10;
			term /= 10;
		}
		if (divsum == n) {
			cout << i;
			break;
		}
		if (i==n) cout << 0;
	}
}

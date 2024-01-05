#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;



int main() {
	int N;
	int cnt = 0;
	cin >> N;
	N--;
	cnt++;
	int i = 1;
	while (N > 0) {
		N -= i * 6;
		cnt++;
		i++;
	}
	cout << cnt;
	cin >> N;
}
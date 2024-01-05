#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;



int main() {
	int N;
	cin >> N;
	int i = 1;
	int num;
	int sum;
	while (N > i) {
		num = i;
		sum = 0;
		while (num) {
			sum += num % 10;
			num = num / 10;
		}
		if (N == sum + i) {
			cout << i;
			break;
		}
		i++;
	}
	if (N <= i) {
		cout << 0;
	}
}
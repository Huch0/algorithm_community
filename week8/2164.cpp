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
	std::queue<int> Cards;
	int i;
	for (i = 0; i < N; i++) {
		Cards.push(i + 1);
	}
	int back;
	while (Cards.size() != 1) {
		Cards.pop();
		if (Cards.size() == 1) {
			break;
		}
		back = Cards.front();
		Cards.pop();
		Cards.push(back);
	}
	cout << Cards.front();
}
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

int main() {
	int n;
	cin >> n;
	int bags = 0;
	int leftovers = 0;
	bags = n / 5;
	leftovers = n % 5;
	while (bags>=0) {
		if (leftovers%3 == 0) {
			bags += leftovers / 3;
			break;
		}
		bags--;
		leftovers += 5;
	}
	if (!bags) {
		bags--;
	}
	
	cout << bags;
	cin >> n;
}
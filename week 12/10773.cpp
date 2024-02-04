#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
using namespace std;



int main() {
	int n;
	int temp;
	cin >> n;
	stack <int> income;
	while (n) {
		cin >> temp;
		n--;
		if (temp == 0) {
			income.pop();
		}
		else {
			income.push(temp);
		}	
	}
	n = 0;
	while (!income.empty()) {
		temp = income.top();
		income.pop();
		n += temp;
	}
	cout << n;
	cin >> n;
}

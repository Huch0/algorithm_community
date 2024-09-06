#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <math.h>
#include <queue>
using namespace std;

int main() {
	int n;
	int k;
	int temp;
	cin >> n >> k;
	vector <int> wires;
	int max_len = 0;
	while (n--) {
		cin >> temp;
		wires.push_back(temp);
		max_len = max(max_len, temp);
	}
	sort(wires.begin(), wires.end());
	long long min = 1;
	long long max = max_len;
	long long mid = (min + max) / 2;
	cout << max << ' ' << mid << ' ' << min << endl;
	while (min <= max) {
		int count = 0;
		for (int wire : wires) {
			count += wire / mid;
		}
		if (count<k) {
			max = mid-1;	
		}
		else {
			min = mid+1;
		}
		mid = (min + max) / 2;
		cout << max << ' ' << mid << ' ' << min << endl;
	}
	cout << mid;
	cin >> max;
}

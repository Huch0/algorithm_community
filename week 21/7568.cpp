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
	int height;
	int weight;
	vector <pair<int, int>> people;
	cin >> n;
	vector <int> count(n, 1);
	while (n--) {
		cin >> weight >> height;
		people.push_back(make_pair(weight, height));
	}
	//n = 0;
	for (int i = 0;i < people.size() - 1;i++) {
		for (n = i;n < people.size();n++) {
			if (people[i].first > people[n].first && people[i].second > people[n].second) {
				count[n]++;
			}
			else if (people[i].first < people[n].first && people[i].second < people[n].second) {
				count[i]++;
			}
		}
	}
	for (int num : count) {
		cout << num << ' ';
	}
	cin >> n;
}
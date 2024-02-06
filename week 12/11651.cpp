#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
using namespace std;

bool increase(pair <int,int> a, pair <int, int> b) {
	if (a.second == b.second) {
		return a.first < b.first;
	}
	return a.second < b.second;
}

int main() {
	int n;
	int a;
	int b;
	cin >> n;
	pair <int, int> coordinate;
	vector <pair<int,int>> coordinates;
	while (n) {
		cin >> a>>b;
		n--;
		coordinate = make_pair(a, b);
		coordinates.push_back(coordinate);
	}
	sort(coordinates.begin(), coordinates.end(), increase);
	for (pair<int,int> pairs : coordinates) {
		cout << pairs.first << ' ' << pairs.second << '\n';
	}
	cin >> n;
}

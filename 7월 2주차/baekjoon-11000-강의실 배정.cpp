#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
	int n, answer = 0;
	cin >> n;
	vector<pair<int, int>> a;
	vector<int> rooms;
	for (int i=0; i<n; i++) {
		pair<int, int> p;
		cin >> p.first >> p.second;
		a.push_back(p);
	}

	sort(a.begin(), a.end(), [](pair<int, int> a, pair<int, int> b){return a.second<b.second;});
	multiset<int> s;
	s.insert(a[0].second);
	for (int i=1; i<a.size(); i++) {
		auto it = s.rbegin();
		for (; it != s.rend(); it++) {
			if (a[i].first >= *it) break;
		}
		if (it == s.rend()) s.insert(a[i].second);
		else {
			s.erase(--it.base());
			s.insert(a[i].second);
		}
	}
	cout << s.size();
}

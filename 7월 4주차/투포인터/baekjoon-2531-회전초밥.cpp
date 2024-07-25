#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N, d, k, c;
	cin >> N >> d >> k >> c;
	vector<int> a(N);
	for (int i=0; i<N; i++) cin >> a[i];
	for (int i=0; i<k; i++) {
		a.push_back(a[i]);
	}
	N += k;

	int answer = 0;
	unordered_set<int> myset;
	vector<int> count(d+1, 0);
	for (int i=0; i<k; i++) {
		if (a[i] != c) {
			myset.insert(a[i]);
			count[a[i]]++;
		} 
	}
	answer = myset.size();

	int start = 0, end = k;
	while (end < N-1) {
		count[a[start]]--;
		if (count[a[start]] == 0) myset.erase(a[start]);
		start++;
		if (a[end] != c) {
			count[a[end]]++;
			myset.insert(a[end]);
		}
		end++;

		answer = max(answer, (int)myset.size());
	}
	cout << answer + 1;
}

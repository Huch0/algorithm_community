#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	int n;
	cin >> n;
	vector<int> d(n-1);
	vector<int> price(n);
	for (int i=0; i<n-1; i++) cin >> d[i];
	for (int i=0; i<n; i++) cin >> price[i];
	
	long long answer = 0;
	while(!d.empty()) {
		auto iter = min_element(price.begin(), price.end()-1);
		int curindex = distance(price.begin(), iter);
		long long curleftdistance = 0;
		for (int i=curindex; i<d.size(); i++) {
			curleftdistance += d[i];
		}

		answer += (*iter)*curleftdistance;
		d.erase(d.begin()+curindex, d.end());
		price.erase(price.begin()+curindex+1, price.end());
	}
	cout << answer;
}

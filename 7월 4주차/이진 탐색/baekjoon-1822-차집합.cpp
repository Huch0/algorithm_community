#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<int> a(n);
	vector<int> b(m);
	for (int i=0; i<n; i++) cin >> a[i];
	for (int i=0; i<m; i++) cin >> b[i];

	sort(b.begin(), b.end());
	vector<int> answer;
	for (int i=0; i<n; i++) {
		if (!binary_search(b.begin(), b.end(), a[i])) answer.push_back(a[i]);
	}
	
	sort(answer.begin(), answer.end());
	cout << answer.size() << endl; 
	for (int i=0; i<answer.size(); i++) cout << answer[i] << " ";
}

// 왜 hash를 이용한게 더 느릴까? -> 해시 충돌 때문 ! 50만개 정도의 데이터를 set에 담으면 충돌 때문에 효율이 매우 떨어진다. 
/*
int main() {
   int n, m; cin >> n >> m;
   vector<int> a(n);
   unordered_set<int> b;
   for (int i=0; i<n; i++) cin >> a[i];
   for (int i=0; i<m; i++) {
      int k; cin >> k;
      b.insert(k);
   }
   
   vector<int> answer;
   for (int i=0; i<n; i++) {
      if (b.find(a[i]) == b.end()) answer.push_back(a[i]);
   }
   
   sort(answer.begin(), answer.end());
   cout << answer.size() << endl; 
   for (int i=0; i<answer.size(); i++) cout << answer[i] << " ";
}
*/

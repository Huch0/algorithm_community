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

// �� hash�� �̿��Ѱ� �� ������? -> �ؽ� �浹 ���� ! 50���� ������ �����͸� set�� ������ �浹 ������ ȿ���� �ſ� ��������. 
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

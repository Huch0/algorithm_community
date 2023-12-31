#include <bits/stdc++.h>
using namespace std;

int main() {
	multimap<set<int>, int> database;
	string command;
	
	while(true) {
		cin >> command;
		if (command == "R") {
			set<int> code;
			int n;
			while(true) { 
				cin >> n;
				if (n < 0) break;
				code.insert(n);
			}
			database.insert({code, n});
		}
		else if (command == "Q") {
			set<int> code;
			int n;
			priority_queue<int> answer;
			while(true) {
				cin >> n;
				if (n == 0) break;
				code.insert(n);
			}
			auto range = database.equal_range(code);
			for (auto it = range.first; it != range.second; it++) {
				answer.push(it->second);			
			}
			if (range.first == range.second) cout << "None\n";
			else {
				while(!answer.empty()) {
					cout << answer.top() << " ";
					answer.pop();
				}
				cout << endl;
			}
		}
		else break;
	}
	
}

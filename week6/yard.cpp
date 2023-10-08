#include <bits/stdc++.h>
using namespace std;

void getInput(int num_of_section, deque<int> section[]) {
	int num_of_container, w;
	for (int i=0; i<num_of_section; i++) {
		cin >> num_of_container;
		for (int j=0; j<num_of_container; j++) {
			cin >> w;
			section[i].push_back(w);
		}
	}
}
void movingProcess(int num_of_section, deque<int> section[]) {
	while(true) {
		int h=0, l=999999, index_tomove, index_dest;
		for (int i=0; i<num_of_section; i++) {
			if (section[i].size() > h || ( (h != 0 && section[i].size() == h) && (section[i].back() > section[index_tomove].back())) ) {
				index_tomove = i;
				h = section[i].size();
			}
			if (section[i].size() < l) {
				index_dest = i;
				l = section[i].size();
			}
		}
		if (h - l <= 1) return;
		section[index_dest].push_back(section[index_tomove].back());
		section[index_tomove].pop_back();
	}
}
void printState(int num_of_section, deque<int> section[]) {
	for (int i=0; i<num_of_section; i++) {
		for (int weight : section[i]) cout << weight << " ";
		if (section[i].size() == 0) cout << "0";
		cout << "\n";
	}
}

int main() {
	int num_of_section;
	cin >> num_of_section;
	deque<int> section[num_of_section];

	getInput(num_of_section, section);
	movingProcess(num_of_section, section);
	printState(num_of_section, section);
}

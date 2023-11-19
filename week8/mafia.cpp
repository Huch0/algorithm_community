#include <bits/stdc++.h>
using namespace std;

void get_mafia_info(map<string, vector<string>>& list) {
	int n;
	string person, boss;
	cin >> n;

	for (int i=0; i<n-1; i++) {
		cin >> person >> boss;
		if (list.find(person) == list.end()) {
			list[person] = vector<string>();
		}
		
		if (list.find(boss) == list.end()) {
			list[boss] = vector<string>();
		}
		list[boss].push_back(person);
	}
}

int get_subnum(string key, map<string, array<int, 2>>& info, map<string, vector<string>>& list) {
	if (info.find(key) != info.end()) return info[key][0];
	else {
		if (list[key].size() == 0) {
			info[key][0] = 0;
			return 0;
		}
		else {
			int subnum = 0;
			for (auto m : list[key]) {
				subnum += get_subnum(m, info, list) + 1;
			}
			return subnum;
		}
	}
}

void calculate_subnum(map<string, array<int, 2>>& info, map<string, vector<string>>& list) {
	for (auto row : list) {
		int num = get_subnum(row.first, info, list);
		info[row.first] = array<int, 2>{num, -1};
	}
}

string find_boss(map<string, array<int, 2>>& info) {
	int max = 0;
	string boss;
	for (auto i : info) {
		if (i.second[0] > max) {
			max = i.second[0];
			boss = i.first;
		}
	}
	return boss;
}

void calculate_depth(string key, map<string, array<int, 2>>& info, map<string, vector<string>>& list, int depth) {
	info[key][1] = depth;
	for (auto member : list[key]) {
		calculate_depth(member, info, list, depth+1);
	}
}

bool mysort(pair<string, array<int, 2>> a, pair<string, array<int, 2>> b) {
	if (a.second[0] != b.second[0]) return a.second[0] > b.second[0];
	else if (a.second[1] != b.second[1]) return a.second[1] < b.second[1];
	else return a.first < b.first;
}

void print_order(map<string, array<int, 2>>& info) {
	vector<pair<string, array<int, 2>>> vinfo (info.begin(), info.end());
	sort(vinfo.begin(), vinfo.end(), mysort);
	for (auto m : vinfo) {
		cout << m.first << "\n";
	}
}

int main() {
	map<string, vector<string>> subordinate_list;
	map<string, array<int, 2>> info;

	get_mafia_info(subordinate_list);
	calculate_subnum(info, subordinate_list);
	string boss = find_boss(info);
	calculate_depth(boss, info, subordinate_list, 0);
	print_order(info);
}


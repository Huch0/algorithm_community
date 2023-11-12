#include <bits/stdc++.h>
using namespace std;
typedef vector<pair<string, array<int, 2>>> tablevec;
typedef array<int, 2> int2array;

void write(tablevec& file_table, int& capacity) {
	string name;
	int size;
	cin >> name >> size;
	auto dupcheck = find_if(file_table.begin(), file_table.end(), [&](pair<string, int2array> info){return !info.first.compare(name);});
	if (file_table.end() != dupcheck) {
		cout << "error\n"; return;
	}
	if (size > capacity) {
		cout << "diskfull\n";
		return;
	}

	capacity -= size;
	for (int i=0; i<file_table.size()-1; i++) {
		int front_file = file_table[i].second[1];
		int back_file = file_table[i+1].second[0];

		if (size <= back_file - front_file - 1) {
			file_table.insert(file_table.begin() + i + 1, make_pair(name, int2array{front_file + 1, front_file + size}));
			return;
		}
	}

	for (int i=0; i<file_table.size()-1; i++) {
		int front_file = file_table[i].second[1];
		int back_file = file_table[i+1].second[0];
		if (back_file - front_file == 1) continue;

		if (size <= back_file - front_file - 1) {
			file_table.insert(file_table.begin() + i + 1, make_pair(name, int2array{front_file + 1, front_file + size}));
			return;
		}
		file_table.insert(file_table.begin() + i + 1, make_pair(name, int2array{front_file + 1, back_file - 1}));
		size -= back_file - front_file - 1;
	}
}

void del(tablevec& file_table, int& capacity) {
	string name;
	cin >> name;
	auto it = remove_if(file_table.begin(), file_table.end(), [&](pair<string, int2array> info){
		if (!info.first.compare(name)) {
			capacity += info.second[1] - info.second[0] + 1;
			return 1;
		}
		return 0;
	});
	if (it == file_table.end()) cout << "error\n";
	else file_table.erase(it, file_table.end());
}

void show(tablevec& file_table) {
	string name;
	bool find_flag = false;
	cin >> name;
	for_each(file_table.begin(), file_table.end(), [&](pair<string, int2array> info){
		if(!info.first.compare(name)) {
			find_flag = true;
			cout<<info.second[0]<<" ";
		}
	});
	if (!find_flag) cout << "error\n";
	else cout << "\n";
}

void compact(tablevec& file_table) {
	for (int i=1; i<file_table.size()-1; i++) {
		int space = file_table[i].second[0] - file_table[i-1].second[1] - 1;
		file_table[i].second[0] -= space;
		file_table[i].second[1] -= space;

		if (!file_table[i-1].first.compare(file_table[i].first)) {
			file_table[i-1].second[1] = file_table[i].second[1];
			file_table.erase(file_table.begin() + i);
			i--;
		}
	}
}

int main() {
	int capacity;
	string command;
	tablevec file_table;
	cin >> capacity;
	file_table.push_back(make_pair("", int2array{-1, -1}));
	file_table.push_back(make_pair("", int2array{capacity, capacity}));
	while (true) {
		cin >> command;
		if (!command.compare("write")) write(file_table, capacity);
		else if (!command.compare("delete")) del(file_table, capacity);
		else if (!command.compare("show")) show(file_table);
		else if (!command.compare("compact")) compact(file_table);
		else if (!command.compare("end")) break;
	}
}

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>;
using namespace std;

vector <string> words;

bool compare(string a, string b) {
	if (a.size() == b.size()) {
		return a < b;
	}
	else {
		return a.length() < b.length();
	}

}


int main() {
	int num;
	string temp;
	cin >> num;


	for (int i = 0; i < num; i++) {
		cin >> temp;
		words.push_back(temp);
	}

	sort(words.begin(), words.end(), compare);


	for (int j = 0; j < num; j++) {
		cout << words[j] << "\n";
	}




}

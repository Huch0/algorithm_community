#include <iostream>
#include <vector> 
#include <string>
using namespace std;

vector<int> getPi(string str) {
	vector<int> pi(str.length(), 0);
	int j=0;
	for (int i=1; i<str.length(); i++) {
		while(j > 0 && str[j] != str[i]) {
			j = pi[j-1];
		}
		if (str[j] == str[i]) j++;
		pi[i] = j;
	}
	return pi;
}

int main() {
	string text, pattern;
	getline(cin, text);
	getline(cin, pattern);
	
	vector<int> pi = getPi(pattern);
	vector<int> answer;
	
	int j=0;
	for (int i=0; i<text.size(); i++) {
		while (j > 0 && text[i] != pattern[j]) {
			j = pi[j-1];
		}
		if (text[i] == pattern[j]) j++;
		if (j == pattern.size()) {
			answer.push_back(i-j+2);
			j = pi[j-1];
		}
	}
	
	cout << answer.size() << endl;
	for (int i=0; i<answer.size(); i++) {
		cout << answer[i] << " ";
	}
}

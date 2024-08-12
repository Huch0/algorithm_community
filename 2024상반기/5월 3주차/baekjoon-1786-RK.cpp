#include <iostream>
#include <string>
#include <math.h>
#include <vector>
#include <map>
using namespace std;

int main() {
	string text, pattern;
	getline(cin, text);
	getline(cin, pattern);
	int n = text.length(), m = pattern.length();
	//
	vector<int> answer;
	//

	int prime = 7919;
	map<char, int> alphabet;
	int index = 0;
	for (int i=0; i<n; i++) {
		if (alphabet.count(text[i]) > 0) continue;
		alphabet[text[i]] = index;
		index++;
	}

	vector<int> A(n, 0);
	int targetN = 0, a1 = 0, d = alphabet.size();
	int dp = 1;
	for (int i=0; i<m-1; i++) { // dp = d^(m-1)
		dp = dp*d%prime;
	}
	for (int i=0; i<m; i++) {
		targetN = (targetN*d + alphabet[pattern[i]]) % prime;
		a1 = (a1*d + alphabet[text[i]]) % prime;
	}
	A[0] = a1;
	
	for (int i=1; i<n-m+1; i++) {
		A[i] = (d*(A[i-1] - dp*alphabet[text[i-1]]%prime + prime) + alphabet[text[i+m-1]]) % prime;
	}
	
	for (int i=0; i<n-m+1; i++) {
		if (A[i] == targetN) {
			int j, index=0;
			for (j=i; j<i+m; j++, index++) {
				if (text[j] != pattern[index]) break;
			}
			if (index == m) answer.push_back(i+1);
		}
	}
	
	cout << answer.size() << endl;
	for (int i=0; i<answer.size(); i++) {
		cout << answer[i] << " ";
	}
}

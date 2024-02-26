#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <math.h>
#include <queue>
using namespace std;



int main() {
	string expression;
	cin >> expression;
	queue <char> signs;

	int change = 0;
	string num = "";
	char lastSign='+';
	int minAnswer = 0;

	for (char& c : expression) {
		if (c == '+' || c == '-') {
			if (c == '-') {
				change = 1;
				if (lastSign == '+') {
					minAnswer += stoi(num);
				}
				else {
					minAnswer -= stoi(num);
				}
				num = "";
				lastSign = '-';
			}
			else {
				if (change) {
					if (lastSign == '+') {
						minAnswer += stoi(num);
					}
					else {
						minAnswer -= stoi(num);
					}
					num = "";
					lastSign = '-';
				}
				else {
					if (lastSign == '+') {
						minAnswer += stoi(num);
					}
					else {
						minAnswer -= stoi(num);
					}
					num = "";
					lastSign = '+';
				}
			}
		}
		else {
			num += c;
		}
	}
	if (lastSign == '+') {
		minAnswer += stoi(num);
	}
	else {
		minAnswer -= stoi(num);
	}
	cout << minAnswer;
	cin >> num;
}
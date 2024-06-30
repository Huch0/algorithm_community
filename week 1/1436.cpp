#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
int n;

int main() {
	cin >> n;
	int cnt = 0;
	int i = 1;
	while (n != cnt) {
		int temp = i;
		while (temp) {
			if (temp % 1000 == 666) { // check if the last 3 digits are 666
				cnt++;//if they are, break and add count
				break;
			}
			else {
				temp = temp / 10; //if not, divide to check the next 3 consecutive 3 digits
			}
		}
		i++;// check every positive integer starting from 1
	}
	cout << i - 1;
}

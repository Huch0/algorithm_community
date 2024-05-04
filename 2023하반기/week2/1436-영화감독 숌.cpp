#include <iostream>
using namespace std;
int main() {
	int n, i=665, is_endnumber, count = 0;
	cin >> n;
	
	while(true) {
		i++;
		is_endnumber = i;
		while(true) {
			if (is_endnumber % 1000 % 666 == 0 && is_endnumber % 1000 != 0) {
				count++;
				break;
			}
			is_endnumber /= 10;
			if (is_endnumber < 666) break;
		}
		if (count == n) {
			cout << i;
			break;
		}
	}
	
	
}

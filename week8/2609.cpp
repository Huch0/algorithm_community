#include <iostream>
#include <vector>
using namespace std;



int main() {
	int a;
	int b;
	cin >> a;
	cin >> b;

	int i = 1;
	int GCD = 0;
	while (i <= a && i <= b) {
		if (a % i == 0 && b % i == 0) {
			GCD = i;
		}
		i++;
	}
	cout << GCD << endl;

	a = a / GCD;
	b = b / GCD;
	cout << GCD * a * b << endl;

}
#include <iostream>
using namespace std;

int main() {
	int toDeliver;
	cin >> toDeliver;
	
	for (int i = toDeliver/5; i>=0; i--) {
		if ((toDeliver - i*5) % 3 == 0) {
			cout << i + ((toDeliver - i*5)/3);
			break;
		}
		else if (i == 0) cout << -1;
	}
}

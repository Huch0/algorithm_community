#include <iostream>
#include <vector>
using namespace std;

int main() {
	string str;
	cin >> str;
	
	int ans1 = 0, ans2 = 0, flag = -1;
	for (int i=0; i<str.length(); i++) {
		if (str[i] == '0' && flag != 0) {
			flag = 0;
			ans1++;
		}
		else if (str[i] == '1' && flag != 1) {
			flag = 1;
			ans2++;
		}
	}
	if (min(ans1, ans2) != 0 && str[0] != str[str.length()-1]) cout << max(ans1, ans2);
	else cout << min(ans1, ans2);
}

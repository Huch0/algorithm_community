#include <bits/stdc++.h>
using namespace std;

struct f {
	int type; // 0=digit, -1='(', 1=')'
	long x;
	long y;
	f(int type, long x, long y) : type(type), x(x), y(y) {}
};

ostream& operator << (ostream& os, f& fraction) {
	long gcd = __gcd(fraction.x, fraction.y);
	os << fraction.x/gcd << " " << fraction.y/gcd;
	return os;
}

int main() {
	int n;
	char c;
	vector<f> input;
	
	cin >> n;
	for (int i=0; i<n; i++) {
		cin >> c;
		if (c == '(') input.push_back(f(-1,0,0));
		else if (c == ')') input.push_back(f(1,0,0));
		else if ('1' <= c && c <= '9') input.push_back(f(0,c-48,1));
		else {
			cout << "-1";
			return 0;
		}
	}

	int vector_size = 0;
	while (true) {
		if (input.size() == 1) {
			cout << input[0];
			break;
		}
		else if (input.size() == vector_size) {
			cout << "-1";
			break;
		}
		vector_size = input.size();
		
		long a,b,c,d,e,f, count = 0;
		for (int i=0; i<input.size(); i++) {
			if (input[i].type == -1) count = 0;
			else if (input[i].type == 0) count++;
			else {
				if (count == 3) {
					a = input[i-3].x;
					b = input[i-3].y;
					c = input[i-2].x;
					d = input[i-2].y;
					e = input[i-1].x;
					f = input[i-1].y;
					input[i-4].type = 0;
					input[i-4].x = a*d*e + b*c*f;
					input[i-4].y = b*d*e;
					input.erase(input.begin() + i-3, input.begin() + i+1);
					i -= 4;
					count = 0;
				}
				else count = 0;
			}
		}
	}
}

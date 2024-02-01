#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

int main() {
	int a;
	int b;
	int v;
	cin >> a >> b >> v;
	int day = 1;
	int sum = 0;
	v -= a;
	a -= b;
	day = (v+(a-1)) / a;
	cout << ++day;
	cin >> a;

}

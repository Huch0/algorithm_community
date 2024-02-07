#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <math.h>
using namespace std;


int main() {
	int n;
	size_t r=31;
	int M = 1234567891;
	string word;
	cin >> n;
	cin >> word;
	size_t sum = word[0]-'a'+1;
	for (int i = 1; i < n;i++) {
		sum += ((word[i] - 'a'+1)%M) * (r%M);
		r = r % M;
		r = r * 31;
		sum = sum % M;
	}
	cout << sum;
	cin >> n;
}

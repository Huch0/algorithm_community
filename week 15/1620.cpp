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
#include <unordered_map>
using namespace std;



int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int N;
	int M;
	cin >> N >> M;
	vector <string> pokedex(N+1);
	unordered_map <string, int> pokenum;
	string temp;
	for (int i = 1;i < N + 1;i++) {
		cin >> temp;
		pokedex[i] = temp;
		pokenum[temp] = i;
	}
	while (M--) {
		cin >> temp;
		if (isdigit(temp[0])) {
			cout << pokedex[stoi(temp)] << '\n';
		}
		else {
			cout << pokenum[temp] << '\n';
		}
	}
	cin >> temp;
}
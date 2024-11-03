#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
여기선 연산자의 종류가 4개지만, 무한 개로 일반화했을 때는 중복되는 숫자가 있는 순열로 생각해 볼 수 있다. (N과 M 9번문제)
-> 순열을 구하는 기본적인 재귀 로직에서, for문을 돌면서 이전 반복과 같은 수를 만나면 continue하는 방법으로 해결
n-1번 자리까지의 수가 정해졌을 때 n번째 자리에 오는 숫자가 중복되면 안 되기 때문

이 문제에서는 수의 종류가 4개밖에 없기 때문에 각 수가 몇 개인지 저장하는 변수를 만들어서 해결했음

이런 류의 문제가 backtracking, 재귀를 이용해서 풀린다는 것을 기억해주기 
*/

int a, b, c, d;
vector<int> nums;
vector<int> oper;
int maxans = -1000000001;
int minans = 1000000001;

void calc() {
	int answer = nums[0];
	for (int i=1; i<nums.size(); i++) {
		if (oper[i-1] == '+') {
			answer += nums[i];
		}
		else if (oper[i-1] == '-') {
			answer -= nums[i];
		}
		else if (oper[i-1] == 'x') {
			answer *= nums[i];
		}
		else {
			answer /= nums[i];
		}
	}
	maxans = max(maxans, answer);
	minans = min(minans, answer);
}
void dfs() {
	if (nums.size()-1 == oper.size()) {
		calc();
		return;
	}
	
	if (a>0) {
		oper.push_back('+');
		a--;
		dfs();
		oper.pop_back();
		a++;
	}
	if (b>0) {
		oper.push_back('-');
		b--;
		dfs();
		oper.pop_back();
		b++;
	}
	if (c>0) {
		oper.push_back('x');
		c--;
		dfs();
		oper.pop_back();
		c++;
	}
	if (d>0) {
		oper.push_back('/');
		d--;
		dfs();
		oper.pop_back();
		d++;
	}
}

int main() {
	int n; cin >> n;
	for (int i=0; i<n; i++) {
		int k; cin >> k;
		nums.push_back(k);
	}
	cin >> a >> b >> c >> d;
	dfs();
	cout << maxans << " " << minans;
}

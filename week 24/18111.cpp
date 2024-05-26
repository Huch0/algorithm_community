#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <deque>
#include <utility>

#define MIN 0
#define MAX 10000000
using namespace std;
typedef unsigned long long int ll;
int map[501][501];
int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int n, m, b, minTime = 99999999, maxHeight = 0;
	cin >> n >> m >> b;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> map[i][j];
		}
	}

	for (int k = 0; k <= 256; k++)
	{
		int havetodig = 0, havetostack = 0;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (map[i][j] > k)
					havetodig += map[i][j] - k;
				else if (map[i][j] < k)
					havetostack += k - map[i][j];
			}
		}
		if (havetodig + b >= havetostack)
		{
			if (minTime >= havetodig * 2 + havetostack)
			{
				minTime = havetodig * 2 + havetostack;
				maxHeight = k;
			}
		}
	}
	cout << minTime << ' ' << maxHeight;
}
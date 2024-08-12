#include <bits/stdc++.h>
#define MAXDIS 10000000001
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	vector<vector<long long>> distance(n+1, vector<long long>(n+1, MAXDIS));
	for (int i=0; i<m; i++) {
		int a, b, c; cin >> a >> b >> c;
		distance[a][b] = min((int)distance[a][b], c);
	}
	for (int i=1; i<=n; i++) {
		distance[i][i] = 0;
	}

	for (int k=1; k<=n; k++) {
		for (int i=1; i<=n; i++) {
			for (int j=1; j<=n; j++) {
				distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]);
			}
		}
	}

	for (int i=1; i<=n; i++) {
		for (int j=1; j<=n; j++) {
			if (distance[i][j] == MAXDIS) cout << "0 ";
			else cout << distance[i][j] << " ";
		}
		cout << "\n";
	}
}


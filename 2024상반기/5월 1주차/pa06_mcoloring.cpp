#include <iostream>
#include <vector>
using namespace std; 
int pruned;
int possible;
bool promising(int level, vector<int>& colors, vector<vector<int> >& graph) {
	pruned++;
	for (int i=0; i<level-1; i++) {
		if (graph[level-1][i] && colors[level-1] == colors[i]) return false;
	}
	return true;
}
void dfs(int level, vector<int>& colors, vector<vector<int> >& graph, int m) {
	if (promising(level, colors, graph)) {
		if (level == colors.size()) {
			vector<int> colorNtest(m, 0);
			for (int i=0; i<colors.size(); i++) {
				colorNtest[colors[i]] = 1;
			}
			for (int i=0; i<colorNtest.size(); i++) {
				if (colorNtest[i] == 0) return;
			}
			possible++;
		}
		else {
			for (int i=0; i<m; i++) {
				colors[level] = i;
				dfs(level+1, colors, graph, m);
			}
		}
	}
}

int main() {
	int n, m;
	cin >> n >> m;
	
	vector<int> colors(n, -1);
	vector<vector<int> > graph(n, vector<int> (n,0));
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			cin >> graph[i][j];
		}
	}
	
	for (int i=0; i<m; i++) {
		colors[0] = i;
		dfs(1, colors, graph, m);
	}
	
	if (possible == 0) cout << "no";
	else cout << possible << endl << pruned;
}

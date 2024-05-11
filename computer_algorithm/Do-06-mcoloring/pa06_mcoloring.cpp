#include <iostream>
#include <vector>

using namespace std;
int n, m;
int solutionCounter = 0;
int visitedCounter = 0;
vector<int> colored;

bool promising(int i, vector<vector<int>>& adj) {
    int j = 0;
    bool switcher = true;
    while (j < i && switcher) {
        if( adj[i][j] && colored[i] == colored[j] ) switcher = false;
        j++;
    }
    return switcher;
}
bool isFull() {
    vector<bool> check(m+1, false);
    for (int i=0; i<n; i++) check[colored[i]-1] = true;

    for (int i=0; i<m; i++) {
        if( !check[i] ) return false;
    }
    return true;
}
void coloring(int i, vector<vector<int>>& adj) {
    visitedCounter++;
    int color;
    if( promising(i, adj) ) {
        if( i == n-1 ) {
            if( isFull() ) {
                solutionCounter++;
            }
        }
        else {
            for (color = 1; color <= m; color++) {
                colored[i+1] = color;
                coloring(i+1, adj);
            }
        }
    }
    return;
}
int main() {
    cin >> n >> m;
    vector<vector<int>> adjacency(n, vector<int>(n));
    colored.resize(n, 0);
    for (auto &row : adjacency) {
        for (auto &col : row) cin >> col;
    }
    colored[0] = 1;
    coloring(0, adjacency);
    if( solutionCounter == 0 ) cout << "no" << endl;
    else cout << solutionCounter*m << '\n' << visitedCounter*m << endl;
    return 0;
}
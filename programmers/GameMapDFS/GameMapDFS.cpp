#include<vector>
#include <climits>
using namespace std;
vector<pair<int, int>> directions {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
vector<vector<bool>> visited;
vector<vector<int>> minSteps;
int n = 0, m = 0;
void dfs(vector<vector<int>>& maps, pair<int, int> point, int steps) {
    int x = point.first;
    int y = point.second;
    if( x<0 || x>=n || y<0 || y>=m || maps[x][y]==0 || visited[x][y]==true || steps>=minSteps[x][y]) return;
    
    minSteps[x][y] = steps;

    if( x == n-1 && y == m-1) return;
    
    visited[x][y] = true;
    for ( auto d : directions ) {
        dfs(maps, make_pair(x+d.first, y+d.second), steps+1);
    }
    visited[x][y] = false;
    return;
}
int solution(vector<vector<int> > maps)
{
    n = maps.size();
    m = maps[0].size();
    visited.assign(n, vector<bool>(m, false));
    minSteps.assign(n, vector<int>(m, INT_MAX));
    dfs(maps, make_pair(0, 0), 1);
    
    return (minSteps[n-1][m-1] == INT_MAX) ? -1 : minSteps[n-1][m-1];
}
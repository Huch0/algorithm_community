#include <iostream>
#include <map>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>
using namespace std;

int N, M;
map<int, vector<int>> graph;
unordered_set<int> visited;
queue<int> q;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    q.push(1);
    visited.insert(1);

    vector<vector<int>> dist;
    
    while( !q.empty() ) {
        int size = q.size();
        vector<int> temp;
        for (int i=0; i<size; i++) {
            int cur = q.front();
            q.pop();
            temp.push_back(cur);
            for (int next : graph[cur]) {
                if( visited.find(next) == visited.end() ) {
                    visited.insert(next);
                    q.push(next);
                }
            }
        }
        dist.push_back(temp);
    }

    cout << *min_element(dist.back().begin(), dist.back().end()) << ' ' << dist.size()-1 << ' ' << dist.back().size() << '\n';
}
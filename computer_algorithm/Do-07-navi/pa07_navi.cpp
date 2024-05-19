#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;
pair<int, int> start, target;
int m, n;

struct node {
    int f;
    int g;
    int h;
    pair<int, int> pos;
};
vector<node> open;
vector<node> closed;

int h(pair<int, int> p) {
    return static_cast<int>(sqrt(pow(target.first - p.first, 2) + pow(target.second - p.second, 2)));
}

void astar(vector<vector<bool>>& adj) {
    node current = open[0];
    open.erase(open.begin());
    closed.push_back(current);
    
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (auto dir : directions) {
        pair<int, int> next = {current.pos.first + dir.first, current.pos.second + dir.second};
        if( next == target ) {
        cout << (current.g+1) * 3 << "\n";
        return;
    }
        if( next.first < 0 || next.first >= m || next.second < 0 || next.second >= n ) continue;
        if( !adj[next.first][next.second] ) continue;
        node nextNode;
        nextNode.pos = next;
        nextNode.g = current.g + 1;
        nextNode.h = h(next);
        nextNode.f = nextNode.g + nextNode.h;
        bool inOpen = false;
        bool inClosed = false;
        for (auto o : open) {
            if( o.pos == next ) {
                inOpen = true;
                if( o.f > nextNode.f ) {
                    o = nextNode;
                }
            }
        }
        for (auto c : closed) {
            if( c.pos == next ) {
                inClosed = true;
                if( c.f > nextNode.f ) {
                    c = nextNode;
                }
            }
        }
        if( !inOpen && !inClosed ) {
            open.push_back(nextNode);
        }
        sort(open.begin(), open.end(), [](node a, node b) {
            return a.f < b.f;
        });
    }
    astar(adj);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> m >> n;
    vector<vector<bool>> adj(m, vector<bool>(n, true));
    int blocked; cin >> blocked;
    for (int i=0; i<blocked; i++) {
        int zero, x, y; cin >> zero >> x >> y;
        adj[x][y] = false;
    }
    char s; cin >> s;
    cin >> start.first >> start.second;
    char t; cin >> t;
    cin >> target.first >> target.second;

    string ob; cin >> ob;
    int obstacle; cin >> obstacle;
    for (int i=0; i<obstacle; i++) {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        for (int j=x1; j<=x2; j++) {
            for (int k=y1; k<=y2; k++) {
                adj[j][k] = false;
            }
        }
    }

    node startNode;
    startNode.pos = start;
    startNode.g = 0;
    startNode.h = h(start);
    startNode.f = startNode.g + startNode.h;
    open.push_back(startNode);
    astar(adj);

}
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int N, K; cin >> N >> K;
    queue<pair<int, int>> q;
    q.push({N, 0});
    vector<bool> visited(100001, false);
    visited[N] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int steps = q.front().second;
        q.pop();

        if( x == K ) {
            cout << steps << endl;
            break;
        }
        if( x+1 >= 0 && x+1 <= 100000 && visited[x+1] == false ) {
            q.push({x+1, steps+1});
            visited[x+1] = true;
        }
        if( x-1 >= 0 && x-1 <= 100000 && visited[x-1] == false ) {
            q.push({x-1, steps+1});
            visited[x-1] = true;
        }
        if( 2*x >= 0 && 2*x <= 100000 && visited[2*x] == false ) {
            q.push({2*x, steps+1});
            visited[2*x] = true;
        }
    }

}
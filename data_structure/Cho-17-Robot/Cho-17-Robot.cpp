#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

vector<vector<int>> factory;
queue<pair<pair<int, int>, pair<int, bool>>> myQ;
map<pair<pair<int, int>, bool>, pair<bool, int>> visited;
vector<int> result;
int N, t;


void nextBreadth(pair<pair<int, int>, pair<int, bool>> present) {
    if( present.first == make_pair(N-1, 0) ) {
        if( factory[N-2][0] == 0 ) myQ.push(make_pair(make_pair(N-2, 0), make_pair(1, true)));
        if( factory[N-1][1] == 0 ) myQ.push(make_pair(make_pair(N-1, 1), make_pair(1, false)));
        return;
    }
    pair<int, int> now = present.first;
    int row = now.first;
    int column = now.second;
    int dr[4] = {-1, 0, 1, 0};
    int dc[4] = {0, 1, 0, -1};

    for (int i = 0; i < 4; i++) {
        int newRow = row + dr[i];
        int newColumn = column + dc[i];
        if( newRow < 0 || newRow >= N || newColumn < 0 || newColumn >= N ) continue;
        if( factory[newRow][newColumn] != 1 ) {
            pair<pair<int, int>, pair<int, int>> toQue;
            if( present.second.second != (dr[i] != 0) ) toQue = make_pair(make_pair(newRow, newColumn), make_pair(present.second.first+t+1, !present.second.second));
            else toQue = make_pair(make_pair(newRow, newColumn), make_pair(present.second.first + 1, present.second.second));
            auto visitFinder = visited[make_pair(make_pair(newRow, newColumn), toQue.second.second )];
            if( visitFinder.first == true && visitFinder.second <= toQue.second.first ) continue;
            myQ.push(toQue);
        }
    }

}
void myBFS() {
    myQ.push(make_pair(make_pair(N-1, 0), make_pair(0, 0)));
    visited[make_pair(make_pair(N-1, 0), true)] = make_pair(true, 0);
    visited[make_pair(make_pair(N-1, 0), false)] = make_pair(true, 0);
    while (!myQ.empty()) {
        pair<pair<int, int>, pair<int, int>> present = myQ.front();
        myQ.pop();
        if( present.first == make_pair(0, N-1) ) {
            result.push_back(present.second.first);
            continue;
        }
        visited[make_pair(make_pair(present.first.first, present.first.second), present.second.second)] = make_pair(true, present.second.first);
        nextBreadth(present);
    }
}

int main() {
    cin >> N >> t;
    for (int i = 0; i < N; i++) {
        vector<int> row;
        for (int j = 0; j < N; j++) {
            int temp;
            cin >> temp;
            row.push_back(temp);
        }
        factory.push_back(row);
    }

    myBFS();
    if (result.size() == 0) cout << -1 << endl;
    else {
        int min = *min_element(result.begin(), result.end());
        cout << min << endl;
    }

    return 0;
}

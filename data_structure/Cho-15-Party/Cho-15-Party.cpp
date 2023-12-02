#include <iostream>
#include <vector>
#include <queue>
#include <array>
#include <map>
#include <algorithm>
using namespace std;
#define ALL(X) X.begin(), X.end()

map<char, vector<char>> graph;
array<char, 3> friends;

int getDistanceByBFS(queue<char>& toVisit, vector<char>& visited, char target) {
    int distance = 0;
    while (!toVisit.empty()) {
        int size = toVisit.size();
        for (int i=0; i<size; i++) {
            char current = toVisit.front();
            toVisit.pop();
            if (current == target) {
                while( !toVisit.empty() ) toVisit.pop();
                visited.clear();
                return distance;
            }
            for (char next : graph[current]) {
                if (find(ALL(visited), next) == visited.end()) {
                    toVisit.push(next);
                    visited.push_back(next);
                }
            }
        }
        distance++;
    }
    while( !toVisit.empty() ) toVisit.pop();
    visited.clear();
    return -1;
}

int getTime(int distance) {
    if( distance < 0 ) return -1;
    if( distance == 0 ) return 0;
    return distance * 3 - 2;
}

bool exceptionCase() {
    queue<char> toVisit;
    toVisit.push(friends[0]);
    vector<char> visited;
    if( getDistanceByBFS(toVisit, visited, friends[1]) == -1 ) return true;
    toVisit.push(friends[0]);
    if( getDistanceByBFS(toVisit, visited, friends[2]) == -1 ) return true;
    return false;
}

void printPartyVertex() {
    if( exceptionCase() ) {
        cout << "@\n" << -1 << endl;
        return;
    }
    queue<char> toVisit;
    vector<char> visited;

    char partyVertex;
    int minTime = 1000000;

    for ( auto p : graph ) {
        vector<int> times;
        for (char f : friends) {
            toVisit.push(p.first);
            int time = getTime(getDistanceByBFS(toVisit, visited, f));
            if( time == -1 ) break;
            times.push_back(time);
        }
        if( times.size() != 3 ) continue;
        int maxTime = *max_element(ALL(times));
        if( maxTime < minTime ) {
            minTime = maxTime;
            partyVertex = p.first;
        }
    }

    cout << partyVertex << endl;
    cout << minTime << endl;
}

int main() {
    int N; cin >> N;
    for( int i=0; i<3; i++ ) cin >> friends[i];
    for (int i=0; i<N; i++) {
        char key; cin >> key;
        while (true) {
            char value; cin >> value;
            if (value == '$') break;
            graph[key].push_back(value);
        }
    }

    printPartyVertex();

    return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <cstdlib>
using namespace std;

int getSize(vector<vector<int>>& w, int root, int banned) {
    queue<int> q;
    unordered_set<int> visited;
    q.push(root);
    visited.insert(root);
    int result = 1;
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (auto v : w) {
            if( v.front() == x && v.back() != banned && visited.find(v.back()) == visited.end() ) {
                q.push(v.back());
                visited.insert(v.back());
                result ++;
            }
            if( v.back() == x && v.front() != banned && visited.find(v.front()) == visited.end() ) {
                q.push(v.front());
                visited.insert(v.front());
                result ++;
            }
        }
    }
    return result;
}
int solution(int n, vector<vector<int>> wires) {
    int answer = 999999;
    for (auto v : wires) {
        int size1 = getSize(wires, v.front(), v.back());
        int size2 = getSize(wires, v.back(), v.front());
        int dist = abs(size1-size2);
        if( dist < answer ) answer = dist;
    }
    return answer;
}
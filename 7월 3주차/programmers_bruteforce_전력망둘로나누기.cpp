#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = 999999999;
    vector<set<int>> connection(n+1);
    for (int i=0; i<wires.size(); i++) {
        connection[wires[i][0]].insert(wires[i][1]);
        connection[wires[i][1]].insert(wires[i][0]);
    }
    
    for (int i=0; i<wires.size(); i++) {
        //set에서 요소삭제
        connection[wires[i][0]].erase(wires[i][1]);
        connection[wires[i][1]].erase(wires[i][0]);
        //wires[i][0]부터 bfs로 노드 갯수 세기
        int count = 0;
        vector<int> visited(n+1, 0);
        queue<int> q;
        q.push(wires[i][0]);
        visited[wires[i][0]] = 1;
        while(!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int k : connection[cur]) {
                if (visited[k] == 0) {
                    visited[k] = 1;
                    q.push(k);
                }
            }
            count++;
        }
        answer = min(answer, abs(2*count-n));
        //set에 요소삽입
        connection[wires[i][0]].insert(wires[i][1]);
        connection[wires[i][1]].insert(wires[i][0]);
    }
    return answer;
}
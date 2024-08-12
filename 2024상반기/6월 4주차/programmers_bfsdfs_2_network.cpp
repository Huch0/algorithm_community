// https://school.programmers.co.kr/learn/courses/30/lessons/43162 네트워크
#include <string>
#include <vector>
#include <deque>
using namespace std;

int solution(int n, vector<vector<int>> computers) {
    vector<int> visited(n, 0);
    int answer = 0;
    while(true) {
        int start = -1;
        for (int i=0; i<n; i++) {
            if (visited[i] == 0) {
                start = i;
                break;
            }
        }
        if (start == -1) break;

        answer++;
        deque<int> dq = {start};
        while(!dq.empty()) {
            int cur = dq.front();
            dq.pop_front();
            for (int i=0; i<n; i++) {
                if (computers[cur][i] == 1 && visited[i] == 0) {
                    visited[i] = 1;
                    dq.push_back(i);
                }
            }
        }
    }
    return answer;
}
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct comp {
    bool operator ()(vector<int> &a, vector<int> &b) {
        return a[1]>b[1];
    }
};

int solution(vector<vector<int>> jobs) {
    sort(jobs.begin(), jobs.end(), [](vector<int> &a, vector<int> &b) {
        if (a[0] == b[0]) return a[1]<b[1];
        return a[0]<b[0];
    });
    priority_queue<vector<int>, vector<vector<int>>, comp> pq;
    int index = 0;
    int time = 0;
    int answer = 0;
    
    pq.push(jobs[index++]);
    time = pq.top()[0];
    while(index < jobs.size()) {
        vector<int> cur = pq.top();
        pq.pop();
        time += cur[1];
        answer += time-cur[0];
        while(index < jobs.size() && jobs[index][0] <= time) {
            pq.push(jobs[index++]);
        }
        if (pq.empty() && index < jobs.size()) {
            pq.push(jobs[index++]);
            time = pq.top()[0];
        }
    }
    while(!pq.empty()) {
        vector<int> cur = pq.top();
        pq.pop();
        time += cur[1];
        answer += time-cur[0];
    }

    return answer/jobs.size();
}
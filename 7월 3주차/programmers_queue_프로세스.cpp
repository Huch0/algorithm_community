#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int n = priorities.size();
    int cur = 0, maxindex;
    int maxpri = 0;
    int answer = 1;
    vector<int> visited(n, 0);
    for (int i=0; i<n; i++) {
        maxpri = 0;
        for (int j=0; j<n; j++) {
            if (priorities[(cur+j)%n] > maxpri && visited[(cur+j)%n] == 0) {
                maxpri = priorities[(cur+j)%n];
                maxindex = j;
            }
        }
        cur = (cur+maxindex)%n;
        visited[cur] = 1;
        if (cur == location) return answer;
        answer++;
    }
    return answer;
}
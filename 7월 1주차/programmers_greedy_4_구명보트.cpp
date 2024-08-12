#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end(), greater<int>());
    deque<int> dq(people.begin(), people.end());
    while(dq.size() > 1) {
        if (dq.front() + dq.back() <= limit) {
            dq.pop_front();
            dq.pop_back();
        }
        else {
            dq.pop_front();
        }
        answer++;
    }
    if (dq.size() == 1) answer++;
    return answer;
}
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int size = jobs.size();
    sort(jobs.begin(), jobs.end(), [](auto v1, auto v2){return v1.back()<v2.back();});
    int timer = 0;
    
    while (!jobs.empty()) {
        auto it = find_if(jobs.begin(), jobs.end(), [timer](auto v){return v.front() <= timer;});
        if( it == jobs.end() ) timer = min_element(jobs.begin(), jobs.end())->front();
        else {
            timer += it->back();
            answer += (timer-it->front());
            jobs.erase(it);
        }
    }
    return answer/size;
}
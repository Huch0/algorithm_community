#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int i = 0;
    int maxNice = *max_element(priorities.begin(), priorities.end());
    int size = priorities.size();
    while (true) {
        if( priorities[i] == maxNice ) {
            answer++;
            if( i == location ) break;
            priorities[i] = -1;
            maxNice = *max_element(priorities.begin(), priorities.end());
        }
        else i = (i+1)%size;
    }
    return answer;
}
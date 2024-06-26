// https://school.programmers.co.kr/learn/courses/30/lessons/43165 : 타겟 넘버
#include <string>
#include <vector>
#include <iostream>
using namespace std;

int answer;

void dfs(vector<int> &numbers, int lv, int current, int target) {
    if (lv == numbers.size()) {
        if (current == target) answer++;
        return;
    }
    dfs(numbers, lv+1, current-numbers[lv], target);
    dfs(numbers, lv+1, current+numbers[lv], target);
}
int solution(vector<int> numbers, int target) {
    dfs(numbers, 0, 0, target);
    return answer;
}
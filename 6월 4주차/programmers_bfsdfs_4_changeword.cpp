//https://school.programmers.co.kr/learn/courses/30/lessons/43163 단어변환
#include <string>
#include <vector>
#include <deque>

using namespace std;
int canchange(string a, string b) {
    int k = 0;
    for (int i=0; i<a.length(); i++) {
        if (a[i] != b[i]) k++;
    }
    if (k==1) return true;
    else return false;
}
int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    vector<int> visited(words.size()+1, 0);
    deque<pair<string, int>> dq;
    dq.push_back({begin, words.size()});
    
    while(!dq.empty()) {
        int nodenum = dq.size();
        for (int i=0; i<nodenum; i++) {
            pair<string, int> cur = dq.front();
            if (cur.first == target) return answer;
            dq.pop_front();

            visited[cur.second] = 1;
            for (int i=0; i<words.size(); i++) {
                if (visited[i] == 0 && canchange(cur.first, words[i]))
                    dq.push_back({words[i], i});
            }
        }
        answer++;
    }
    
    return 0;
}
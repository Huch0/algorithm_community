#include <string>
#include <vector>
using namespace std;
int lrmove = 999999999;
void dfs(int curmove, int index, string& name, vector<int>& visited) {
    int endflag = 1;
    for (int i=1; i<name.length(); i++) {
        int rindex = (index+i)%name.length();
        if (name[rindex] != 'A' && visited[rindex] == 0) {
            visited[rindex] = 1;
            dfs(curmove + i, rindex, name, visited);
            visited[rindex] = 0;
            endflag = 0;
            break;
        }
    }
    for (int i=1; i<name.length(); i++) {
        int lindex = (index-i+name.length())%name.length();
        if (name[lindex] != 'A' && visited[lindex] == 0) {
            visited[lindex] = 1;
            dfs(curmove + i, lindex, name, visited);
            visited[lindex] = 0;
            endflag = 0;
            break;
        }
    }
    if (endflag == 1) {
        lrmove = min(lrmove, curmove);
    }
}
int solution(string name) {
    int answer = 0;
    
    vector<int> visited(name.length(), 0);
    visited[0] = 1;
    dfs(0, 0, name, visited);
    
    answer += lrmove;
    for (int i=0; i<name.length(); i++) {
        answer += min(name[i] - 'A', 'Z'+1 - name[i]);
    }

    return answer;
}



// 모범답안 보고 작성한 코드
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int solution(string name) {
    int answer = 0, lrmove = name.length()-1, len = name.length();
    for (int i=0; i<len; i++) {
        int nextvisit = i+1;
        for (; nextvisit<len; nextvisit++) {
            if (name[nextvisit] != 'A') break;
        }
        lrmove = min(lrmove, i + (len-nextvisit) + min(i, len-nextvisit));
    }
    answer += lrmove;
    for (int i=0; i<len; i++) {
        answer += min(name[i] - 'A', 'Z'+1 - name[i]);
    }

    return answer;
}
#include <string>
#include <vector>

using namespace std;
vector<int> ctoi = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
int solution(string name) {
    int answer = 0;
    int length = name.length();
    int moving = length-1;
    for (int i=0; i<length; i++) {
        answer += ctoi[name[i]-'A'];
        int j = i+1;
        while (j < length && name[j] == 'A') j++;
        moving = min(moving, i+length-j+min(i, length-j));
    }
    answer += moving;
    
    return answer;
}
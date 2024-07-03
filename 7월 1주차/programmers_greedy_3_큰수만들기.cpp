#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = number;
    int i;
    for (i=0; i<answer.length()-1; i++) {
        if (answer[i] < answer[i+1]) {
            answer = answer.substr(0, i) + answer.substr(i+1);
            k--;
            if (k==0) break;
            i = i-2;
            if (i<-1) i = -1;
        }
    }

    if (k != 0) {
        answer = answer.substr(0, answer.length()-k);
    }

    return answer;
}

//sol2
string solution(string number, int k) {
    for (int i=0; i<number.length() - k && k != 0; i++) {
        auto iter = max_element(number.begin() + i, number.begin() + i + k + 1);
        if (iter != number.begin() + i) {
            number.erase(number.begin()+i, iter);
            k -= distance(number.begin()+i, iter);
        }
    }
    if (k != 0) {
        number = number.substr(0, number.length()-k);
    }
    return number;
}
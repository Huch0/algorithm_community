#include <iostream>
#include <queue>
using namespace std;
int main() {
    int count = 0;
    int test_case;
    cin >> test_case;
    int n, m, ipt;//문서의 개수, 궁금한 문서 위치, 중요도
    for (int i = 0; i < test_case; ++i) {
        count = 0;
        cin >> n >> m;
        queue<pair<int, int>> q;
        priority_queue<int> pq; // 우선순위 큐
        for (int j = 0; j < n; ++j) {
            cin >> ipt;
            q.push({ j, ipt });
            pq.push(ipt);
        }
        while (!q.empty()) {
            int index = q.front().first;
            int value = q.front().second;
            q.pop();//pop it so you can put it in the back if it's wrong
            if (pq.top() == value) {// if the value, which is the next in queue's priority matches the next priority
                pq.pop();
                ++count;
                if (index == m) {
                    cout << count << endl;
                    break;
                }
            }
            else q.push({ index,value });//if it's now suppose to be printed yet, push it back into the very end
        }
    }
    cin >> n;
}

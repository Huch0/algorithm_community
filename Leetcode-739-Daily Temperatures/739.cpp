#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> s;
        vector<int> res(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++) {
            while (!s.empty()) {
                auto prev = s.top();
                if (prev.first < temperatures[i]) {
                    res[prev.second] = i - prev.second;
                    s.pop();
                } else break;
            }
            s.push({temperatures[i], i});
        }
        return res;
    }
};

// stack을 stack<int>로 만들어서 인덱스만 가지고 다니면 메모리를 더 아낄 수 있을 것 같다.
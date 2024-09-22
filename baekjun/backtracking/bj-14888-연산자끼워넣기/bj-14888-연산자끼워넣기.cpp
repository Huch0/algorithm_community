#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int maxResult = -1000000001;
int minResult = 1000000001;

void backtracking(vector<int>& ops, vector<int>& nums, int idx, int result) {
    if( idx == N ) {
        if( result > maxResult ) maxResult = result;
        if( result < minResult ) minResult = result;
        return;
    }

    for (int i=0; i<4; i++) {
        if( ops[i] > 0 ) {
            ops[i]--;
            switch(i) {
                case 0:
                    backtracking(ops, nums, idx+1, result+nums[idx]);
                    break;
                case 1:
                    backtracking(ops, nums, idx+1, result-nums[idx]);
                    break;
                case 2:
                    backtracking(ops, nums, idx+1, result*nums[idx]);
                    break;
                case 3:
                    backtracking(ops, nums, idx+1, result/nums[idx]);
                    break;
            }
            ops[i]++;
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    vector<int> nums(N);
    for (int i=0; i<N; i++) cin >> nums[i];

    vector<int> operators(4);
    for (int i=0; i<4; i++) cin >> operators[i];

    backtracking(operators, nums, 1, nums[0]);

    cout << maxResult << '\n' << minResult << '\n';
}
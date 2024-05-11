class Solution {
public:
    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](int a, int b) {
            stack<int> sa, sb;
            while (a) {
                sa.push(a % 10);
                a /= 10;
            }
            while (b) {
                sb.push(b % 10);
                b /= 10;
            }
            int aTop, bTop;
            while (!sa.empty() && !sb.empty()) {
                aTop = sa.top(); bTop = sb.top();
                if( aTop != bTop ) {
                    return aTop > bTop;
                }
                sa.pop();
                sb.pop();
            }
            if( sa.empty() ) return aTop > sb.top();
            if( sb.empty() ) return sa.top() > bTop;
            return true;
        });
        string result;
        for (int num : nums) {
            result += to_string(num);
        }
        return result;
    }
};
// wrong answer

// sort(nums.begin(), nums.end(), [](int a, int b) {
//     return to_string(a) + to_string(b) > to_string(b) + to_string(a);
// });
// correct lambda function

// while (result.front() == '0' && result[1] == '0') {
//     result.erase(0, 1);
// }
// exception case: [0, 0] -> "00" -> "0"
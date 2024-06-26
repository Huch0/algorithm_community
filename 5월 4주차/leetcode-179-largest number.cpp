class Solution {
public:
    static bool comparator(int an, int bn) {
        string a = to_string(an);
        string b = to_string(bn);
        string ab = a + b;
        string ba = b + a;
        return stod(ab) > stod(ba);
    }
    string largestNumber(vector<int>& nums) {
        if (count(nums.begin(), nums.end(), 0) == nums.size()) return "0";
        sort(nums.begin(), nums.end(), comparator);
        string answer = "";
        for (int n : nums) answer += to_string(n);
        return answer;
    }
};
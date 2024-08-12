class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> answer;
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){return a[0] < b[0];});
        for (int i=0; i<intervals.size()-1; i++) {
            if (intervals[i][1] >= intervals[i+1][0]) {
                intervals[i+1][0] = intervals[i][0];
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1]);
                intervals[i][0] = -1; // 유효x
            }
        }
        for (int i=0; i<intervals.size(); i++) {
            if (intervals[i][0] != -1) answer.push_back(intervals[i]);
        }
        return answer;
    }
};
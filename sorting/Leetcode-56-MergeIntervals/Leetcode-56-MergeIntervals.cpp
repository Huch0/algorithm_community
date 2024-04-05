class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        sort(intervals.begin(), intervals.end(), [](vector<int> a, vector<int>b) {
            return a[0] < b[0];
        });
        for (auto v : intervals) {
            cout << v[0] << ", " << v[1] << endl;
        }
        int temp = -1;
        for (int i=0; i<intervals.size(); i++) {
            if( i == intervals.size()-1 || intervals[i][1] < intervals[i+1][0] || intervals[i][1] >= intervals[i+1][1]) {
                vector<int> toPush;
                if( temp == -1 ) toPush.push_back(intervals[i][0]);
                else toPush.push_back(temp);
                toPush.push_back(intervals[i][1]);
                result.push_back(toPush);
                temp = -1;
                continue;
            }

            if( temp == -1 ) temp = intervals[i][0];
        }
        return result;
    }
};
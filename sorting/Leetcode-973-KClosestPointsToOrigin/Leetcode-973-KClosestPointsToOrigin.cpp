class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), [](auto a, auto b){
            return pow(a[0],2)+pow(a[1],2) < pow(b[0],2)+pow(b[1],2);
        });

        vector<vector<int>> result(points.begin(), points.begin() + k);

        return result;
    }
};
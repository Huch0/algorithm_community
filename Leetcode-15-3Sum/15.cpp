#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<vector<int>> ans;
        int n = nums.size();

        for (int i = 0; i < n-2; i++) {
            int j = i+1, k = n-1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    ans.insert({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                }
                else if (sum < 0) j++;
                else k--;
            }
        }
        
        return vector<vector<int>>(ans.begin(), ans.end());
    }
};
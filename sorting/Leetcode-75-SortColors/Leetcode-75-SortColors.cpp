class Solution {
public:
    void sortColors(vector<int>& nums) {
        int k = nums.size()-1;
        int j = 0;
        for (int i=0; i<=k; i++) {
            if( nums[i] == 0 ) swap(nums[i], nums[j++]);
            if( nums[i] == 2 ) swap(nums[i--], nums[k--]);
        }
    }
};
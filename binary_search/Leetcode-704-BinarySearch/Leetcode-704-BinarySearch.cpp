class Solution {
public:
    int reculsive_search(vector<int>& nums, int target, int start, int end) {
        if( end < start ) return -1;
        int mid = (start+end)/2;
        if( nums[mid] == target ) return mid;
        else if( target < nums[mid] ) return reculsive_search(nums, target, start, mid-1);
        else return reculsive_search(nums, target, mid+1, end);
    }
    int search(vector<int>& nums, int target) {
        return reculsive_search(nums, target, 0, nums.size()-1);
    }
};
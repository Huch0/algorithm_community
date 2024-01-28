class Solution {
public:
    vector<vector<int>> result;
    
    vector<vector<int>> subsets(vector<int>& nums) {
       vector<int> tmp;
        appendResult(nums,tmp,0);
        return result;
    }
    
    void appendResult(vector<int>&nums,vector<int>& tmp,int start){
        if(start==nums.size()){
            result.push_back(tmp);
            return;
        }
        tmp.push_back(nums[start]);
        appendResult(nums,tmp,start+1);
        tmp.pop_back();
        appendResult(nums,tmp,start+1);
    }
};
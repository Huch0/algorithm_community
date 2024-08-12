//in-place sort

//two pointer
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i0 = 0, i1=0, i2=nums.size()-1;
        while (i1 <= i2) {
            if (nums[i1] == 0) {
                swap(nums[i0++], nums[i1]);
                i1++;
            }
            else if (nums[i1] == 2) {
                swap(nums[i1], nums[i2--]);
            }
            else i1++;
        }
    }
};

//bubble sort
class Solution {
public:
    void sortColors(vector<int>& nums) {
        for (int i=nums.size()-1; i>0; i--) {
            for (int j=0; j<i; j++) {
                if (nums[j] > nums[j+1]) swap(nums[j], nums[j+1]);
            }
        }
    }
};
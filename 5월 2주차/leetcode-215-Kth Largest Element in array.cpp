class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq;
        for (auto n : nums) {
            pq.push(n);
        }
        int n;
        for (int i=0; i<k; i++) {
            n = pq.top();
            pq.pop();
        }
        return n;
    }
};


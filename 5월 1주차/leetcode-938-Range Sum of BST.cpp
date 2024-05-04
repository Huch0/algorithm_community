/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int mrounding(TreeNode* node, int low, int high, int sum) {
        if (node == nullptr) return sum;

        int lsum = sum;
        if (node->val > low) lsum = mrounding(node->left, low, high, sum);

        if (node->val >= low && node->val <= high) lsum += node->val;

        if (node->val >= high) return lsum;
        return mrounding(node->right, low, high, lsum);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        return mrounding(root, low, high, 0);
    }
};
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
    int rounding(TreeNode* node, int n) {
        if (node == nullptr) return n;
        int rsum = rounding(node->right, n);
        node->val += rsum;
        int lsum = rounding(node->left, node->val);
        return lsum;
    }
    TreeNode* bstToGst(TreeNode* root) {
        rounding(root, 0);
        return root;
    }
};
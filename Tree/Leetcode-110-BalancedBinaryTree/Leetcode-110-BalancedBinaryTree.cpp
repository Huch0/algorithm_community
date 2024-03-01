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
    bool isBalanced(TreeNode* root) {
        if( root == nullptr ) return true;
        int diff = getHeight(root->left) - getHeight(root->right);
        if( diff > 1 || diff < -1 ) return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }
    int getHeight(TreeNode* sub) {
        if( sub == NULL ) return 0;
        return max(getHeight(sub->left), getHeight(sub->right))+1;
    }
};
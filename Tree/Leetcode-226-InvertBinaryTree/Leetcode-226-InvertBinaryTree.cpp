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
    TreeNode* invertTree(TreeNode* root) {
        changeBoth(root);
        return root;
    }
    void changeBoth(TreeNode* subtree) {
        if( subtree == nullptr ) return;

        TreeNode* temp = subtree->right;
        subtree->right = subtree->left;
        subtree->left = temp;

        changeBoth(subtree->left);
        changeBoth(subtree->right);

    }
};
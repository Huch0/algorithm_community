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
    int result = 0;
    int longestUnivaluePath(TreeNode* root) {
        myDFS(root, root->val);
        return result;
    }
    int myDFS(TreeNode* root, int rootVal) {
        if( root == NULL ) return 0;
        if( root->val != rootVal ) {
            myDFS(root, root->val);
            return 0;
        }
        int left = myDFS(root->left, rootVal);
        int right = myDFS(root->right, rootVal);
        result = max(result, left+right);
        return max(left, right)+1;
    }
};

//runtime error
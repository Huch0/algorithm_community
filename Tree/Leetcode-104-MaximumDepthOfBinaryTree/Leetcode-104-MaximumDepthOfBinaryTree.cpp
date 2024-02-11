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
    int maxDepth(TreeNode* root, int depth = 1) {
        if(root == nullptr) return 0;
        
        result = max(result, depth);
        if(root->left){
            maxDepth(root->left, depth + 1);
        }
        if(root->right){
            maxDepth(root->right, depth + 1);
        }
        return result;
    }
};
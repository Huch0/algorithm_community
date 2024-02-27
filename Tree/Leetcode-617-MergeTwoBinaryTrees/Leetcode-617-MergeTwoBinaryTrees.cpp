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
    void mergeSubtrees(TreeNode* sub1, TreeNode* sub2, TreeNode* &result) {
        if( !sub1 && !sub2 ) return;
        else if( sub1 && !sub2 ) {
            result = new TreeNode(sub1->val);
            mergeSubtrees(sub1->left, sub2, result->left);
            mergeSubtrees(sub1->right, sub2, result->right);
        }
        else if( !sub1 && sub2 ) {
            result = new TreeNode(sub2->val);
            mergeSubtrees(sub1, sub2->left, result->left);
            mergeSubtrees(sub1, sub2->right, result->right);
        }
        else {
            result = new TreeNode(sub1->val + sub2->val);
            mergeSubtrees(sub1->left, sub2->left, result->left);
            mergeSubtrees(sub1->right, sub2->right, result->right);
        }
    }
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        TreeNode* result(nullptr);
        mergeSubtrees(root1, root2, result);
        return result;
    }
};
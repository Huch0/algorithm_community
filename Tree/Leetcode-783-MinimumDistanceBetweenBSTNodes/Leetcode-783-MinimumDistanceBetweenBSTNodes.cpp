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
    vector<int> vals;
    void pushDatas(TreeNode* subtree) {
        if( subtree == nullptr ) return;
        vals.push_back(subtree->val);
        pushDatas(subtree->left);
        pushDatas(subtree->right);
    }
    int minDiffInBST(TreeNode* root) {
        pushDatas(root);
        sort(vals.begin(), vals.end());
        int result = INT_MAX;
        for (int i=0; i<vals.size()-1; i++) {
            result = min(result, vals[i+1]-vals[i]);
        }

        return result;
    }
};
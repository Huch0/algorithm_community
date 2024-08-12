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
    void midtour(TreeNode* node, int& prev, int& answer) {
        if (node == nullptr) return;

        midtour(node->left, prev, answer);

        int diff = node->val - prev;
        if (diff < answer) answer = diff;
        prev = node->val;

        midtour(node->right, prev, answer);
    }
    int minDiffInBST(TreeNode* root) {
        int prev = -100001, answer = 100001;
        midtour(root, prev, answer);
        return answer;
    }
};
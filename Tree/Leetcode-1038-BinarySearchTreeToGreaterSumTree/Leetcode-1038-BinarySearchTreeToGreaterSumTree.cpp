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
	TreeNode* bstToGst(TreeNode* root) {
		vector<int> valList;
		int index = 0;
		recursiveList(valList, root);
		for (int i = 1; i < valList.size(); ++i) {
			valList[i] += valList[i - 1];
		}
		recursiveChange(valList, root, index);

		return root;
	}

private:
	void recursiveList(vector<int>& valList, TreeNode* node) {
		if( node->right != 0 )
			recursiveList(valList, node->right);
		valList.push_back(node->val);
		if( node->left != 0 )
			recursiveList(valList, node->left);
	}
    
    void recursiveChange(vector<int>& valList, TreeNode* node, int& index) {
		if( node->right != 0 )
			recursiveChange(valList, node->right, index);
		node->val = valList[index++];
		if( node->left != 0 )
			recursiveChange(valList, node->left, index);
	}
};
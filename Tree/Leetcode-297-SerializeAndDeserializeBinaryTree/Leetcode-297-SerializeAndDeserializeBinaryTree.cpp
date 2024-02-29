/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    void serial(TreeNode* node, string& str){
        if(node == nullptr){
            str += "null";
        }else{
            str += to_string(node->val) + ",";
            serial(node->left, str); str += ",";
            serial(node->right, str);
        }
    }
    
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string str = "";
        serial(root, str);
        return str;
    }

    std::vector<std::string> string_split(std::string str, std::string delimiter){
        size_t pos = 0;
        std::string token;
        std::vector<std::string> result;

        while(true){
            pos = str.find(delimiter);
            token = str.substr(0, pos);
            result.push_back(token);
            if(pos == string::npos) break;
            str.erase(0, pos+delimiter.length());
        }
        return result;
    }
    
    TreeNode* deserial(queue<string>& q){
        string token = q.front(); q.pop();
        if(token == "null") return nullptr;
        TreeNode* root = new TreeNode(stoi(token));
        root->left = deserial(q);
        root->right = deserial(q);
        return root;
    };
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> tokens = string_split(data, ",");
        queue<string, deque<string>> q(deque<string>(tokens.begin(), tokens.end()));
        return deserial(q);
    }
};
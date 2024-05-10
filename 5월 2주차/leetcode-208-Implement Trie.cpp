class Trie {
public:
    typedef struct TreeNode {
        char c;
        string data;
        vector<TreeNode*> childnode;
        vector<char> childch;
    } TreeNode;

    TreeNode *root;

    Trie() {
        root = new TreeNode();
    }
    
    void insert(string word) {
        int i = 0;
        TreeNode *node = root;
        while(true) {
            auto iter = find(node->childch.begin(), node->childch.end(), word[i]);
            if (iter == node->childch.end()) break;
            
            int index = distance(node->childch.begin(), iter);
            node = node->childnode[index];
            i++;
        }
        for (; i<word.size(); i++) {
            TreeNode *nptr = new TreeNode();
            nptr->c = word[i];
            node->childnode.push_back(nptr);
            node->childch.push_back(word[i]);
            node = nptr;
        }
        node->data = word;
    }
    
    bool search(string word) {
        TreeNode *node = root;
        for (int i=0; i<word.size(); i++) {
            auto iter = find(node->childch.begin(), node->childch.end(), word[i]);
            if (iter == node->childch.end()) return false;

            int index = distance(node->childch.begin(), iter);
            node = node->childnode[index];
        }
        if (node->data == word) return true;
        else return false;
    }
    
    bool startsWith(string prefix) {
        TreeNode *node = root;
        for (int i=0; i<prefix.size(); i++) {
            auto iter = find(node->childch.begin(), node->childch.end(), prefix[i]);
            if (iter == node->childch.end()) return false;

            int index = distance(node->childch.begin(), iter);
            node = node->childnode[index];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
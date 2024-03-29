class TrieNode{
public:
    vector<TrieNode*> children;
    int index;
    vector<int> palins;
    
    TrieNode(){
        children = vector<TrieNode*>(26);
        index = -1;
    }
};

class Trie{
private:
    TrieNode* root;
    
    bool isPalindrome(string& str, int l, int r){
        for(; l < r; ++l, --r){
            if(str[l] != str[r]){
                return false;
            }
        }
        
        return true;
    };
public:
    Trie(){
        root = new TrieNode();
    }
    
    void add(string& word, int index){
        TrieNode* cur = root;
        
        for(int i = word.size()-1; i >= 0; --i){
            if(isPalindrome(word, 0, i)){
                cur->palins.push_back(index);
            }
            char c = word[i];
            if(cur->children[c-'a'] == nullptr){
                cur->children[c-'a'] = new TrieNode();
            }
            cur = cur->children[c-'a'];
        }
        cur->index = index;
        cur->palins.push_back(index);
    }
    
    void find(string& word, int index, vector<vector<int>>& res){
        TrieNode* cur = root;
        
        for(int i = 0; i < word.size(); ++i){
            if(cur->index != -1 && cur->index != index && isPalindrome(word, i, word.size()-1)){
                res.push_back({index, cur->index});
            }
            
            char c = word[i];
            
            if(cur->children[c-'a'] == nullptr) return;
            
            cur = cur->children[c-'a'];
        }

        for(int palinIndex : cur->palins){
            if(palinIndex == index) continue;
            res.push_back({index, palinIndex});
        }
    }
};

class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        Trie* trie = new Trie();
        int n = words.size();
        
        for(int i = 0; i < n; ++i){
            trie->add(words[i], i);
        }
        
        vector<vector<int>> res;
        
        for(int i = 0; i < n; ++i){
            trie->find(words[i], i, res);
        }
        
        return res;
    }
};
class Trie {
public:
    set<string> words;
    Trie() {
    }

    void insert(string word) {
        words.insert(word);
    }
    
    bool search(string word) {
        return words.find(word)!=words.end();
    }
    
    bool startsWith(string prefix) {
        for(set<string>::iterator it = words.begin(); it!=words.end(); it++){
            if((*it).rfind(prefix, 0) == 0) return true;
        }
        return false;
    }
};
class Solution {
public:
    bool isAnagram(string s, string t) {
        for (char c : s) {
            auto it = find(t.begin(), t.end(), c);
            if (it == t.end()) return false;
            t.erase(it);
        }
        return t.empty();
    }
};
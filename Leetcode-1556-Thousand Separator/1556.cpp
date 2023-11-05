class Solution {
public:
    string thousandSeparator(int n) {
        if (n < 1000) return to_string(n);
        string ans = "";
        string s = to_string(n);

        int cnt = 1;
        for (int i = 0; i < s.length(); i++) {
            ans += s[i];
            if ((s.length() - cnt) % 3 == 0 && i != s.length() - 1) ans += '.'; 
            cnt++;
        }
        return ans;
    }
};
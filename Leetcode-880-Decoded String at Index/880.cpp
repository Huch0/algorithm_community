#include <string>
using namespace std;

class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long length = 0;
        int i = 0;

        while (length < k) {
            if (isdigit(s[i])) length *= s[i] - '0';
            else length++;
            i++;
        }

        for (i -= 1; i >= 0; i--) {
            if (isdigit(s[i])) {
                length /= s[i] - '0';
                k %= length;
            }
            else {
                if (k == 0 || k == length) return string(1, s[i]);
                length--;
            }
        }
        return "";
    }
};
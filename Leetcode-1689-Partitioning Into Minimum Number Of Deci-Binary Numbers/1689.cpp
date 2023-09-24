#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
  int minPartitions(string n) {
    int ans = 1;
    for (char c : n) {
      ans = max(ans, c - '0');
    }
    return ans;
  }
};
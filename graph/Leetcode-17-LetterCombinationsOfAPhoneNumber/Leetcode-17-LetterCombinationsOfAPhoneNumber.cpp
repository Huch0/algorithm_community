class Solution {
    map<char, string> phone = {make_pair('2', "abc"), make_pair('3', "def"), make_pair('4', "ghi"), make_pair('5', "jkl"), make_pair('6', "mno"), make_pair('7', "pqrs"), make_pair('8', "tuv"), make_pair('9', "wxyz")};

public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        myDfs(digits, 0, "", result);

        return result;
    }

    void myDfs(string digits, int index, string myStr, vector<string>& result){
        string target = phone[digits[index]];
        for (char toAppend : target) {
            string newStr(myStr);
            newStr.push_back(toAppend);
            if( index == digits.size()-1 ) result.push_back(newStr);
            else myDfs(digits, index+1, newStr, result);
        }
    }
};
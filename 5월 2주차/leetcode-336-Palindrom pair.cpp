class Solution {
public:
    bool isPal(string& str) {
        for (int i=0; i<str.length() / 2; i++) {
            if (str[i] != str[str.length()-1-i]) return false;
        }
        return true;
    }
    typedef struct TreeNode {
        char c;
        int isEnd = -1; // -1이면 끝이 아니라는 것, 0이상의 수면 words에서의 index를 의미
        map<char, TreeNode*> child;
    } TreeNode;

    // 0. nullptr이면 return한다
    // 1. 자기걸 더한다
    // 2. node가 isEnd라면 지금 str이 회문인지 확인
    // 3. child들에 대해서 dfs를 호출해준다.
    void dfs(TreeNode *node, vector<vector<int>>& answer, int wordidx, string str) {
        if (node == nullptr) return;
        str = str + node->c;
        if (node->isEnd != -1 && isPal(str) && wordidx != node->isEnd) {
            answer.push_back({wordidx, node->isEnd});
        }
        for (auto pair : node->child) {
            dfs(pair.second, answer, wordidx, str);
        }
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        vector<vector<int>> answer;
        TreeNode *root = new TreeNode;

        int wordidx = -1;
        for (string str : words) { // 주어진 word의 뒤부터 trie에 넣기
            wordidx++;
            int i;
            TreeNode *node = root;
            if (str.length() == 0) { // ""에 대한 예외처리
                root->isEnd = wordidx;
                continue;
            }
            for (i=str.length()-1; i>=0; i--) {
                if (node->child.find(str[i]) == node->child.end()) break;
                node = node->child[str[i]];
            }
            for (; i>=0; i--) {
                TreeNode *nptr = new TreeNode;
                nptr->c = str[i];
                node->child[str[i]] = nptr;
                node = nptr;
            }
            node->isEnd = wordidx;
        }

        wordidx = -1;
        int notPalFlag;
        for (string str : words) { // (i,j)가 가능한지 검사. str이 i, trie에 있는게 j
            wordidx++;
            notPalFlag = 0;
            if (str.length() == 0) continue; // ""에 대한 예외처리
            TreeNode *node = root;
            int i=0;
            for (; i<str.length(); i++) {
                if (node->child.find(str[i]) == node->child.end()) {
                    notPalFlag = 1;
                    break;
                } // 다음 i (word)로 넘어가기
                node = node->child[str[i]];
                if (node->isEnd != -1) { // case 1 or 2
                    if (i == str.length()-1 && wordidx != node->isEnd) {
                        answer.push_back({wordidx, node->isEnd}); // case 2
                    }
                    else {
                        string left = str.substr(i+1);
                        if (isPal(left) && wordidx != node->isEnd) {
                            answer.push_back({wordidx, node->isEnd}); // case 1
                        }
                    }
                }
            }
            if (notPalFlag) continue;
            //case 3만 처리해 주면 됌. 1과 2는 for문 안에서 끝났음
            for (auto pair : node->child) {
                dfs(pair.second, answer, wordidx, "");
            }
        }

        if (root->isEnd != -1) { // ""에 대한 예외처리
            for (int i=0; i<words.size(); i++) {
                if (isPal(words[i]) && i != root->isEnd) {
                    answer.push_back({i, root->isEnd});
                    answer.push_back({root->isEnd, i});
                }
            }
        }

        return answer;
    }
};
/*
1. 트라이를 만든다
2. 문자열의 뒤가 root로오게 트라이로 모두 넣는다
3. 맨앞부터 검사하는데, 이말은 즉 검사하는 애가 앞에 오는 i, 트라이에 있는 애가 뒤에 오는 j임을 의미한다
case1
검사하는 애가 더 긴경우
트라이의 리프에 먼저 도달하게됌 > 앞뒤는 일단 일치한다는것. 검사하는 애의 나머지 것들이 회문이면 ok
검사하는 애의 문자열은 들고 잇으니까 판단하기 쉬움
case2
i랑 j의 길이가 같은경우 끝날때 정확히 리프에 있다 -> 바로 ㅇㅋ
case3
트라이에 있는 애가 더 긴경우
검사하는 애가 먼저 끝남 > 트라이에 있는 애의 나머지 것들이 회문이면 ok
트라이의 끝까지 가면 어떤 문자열인지 알수있음 . 이 문자열에서 끝부분을 잘라주고(검사하는 애의 역) 회문인지 검사
*/

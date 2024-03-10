class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 0) return {};
        if (n == 1) return {0};
        
        vector<int> res, degrees(n,0);
        vector<vector<int>> adj(n);
        for (int i=0; i<edges.size(); i++) {
            adj[edges[i][0]].push_back(edges[i][1]);
            adj[edges[i][1]].push_back(edges[i][0]);
            degrees[edges[i][1]]++;
            degrees[edges[i][0]]++;
        }
        queue<int> myQue;
        for (int i=0;i<n;i++) if( degrees[i] == 1 ) myQue.push(i);
        while (!myQue.empty()) {
            res.clear();
            int size=myQue.size();
            for(int i=0; i<size; i++) {
                int cur=myQue.front();
                myQue.pop();
                res.push_back(cur);
                for (auto &neighbor:adj[cur]) {
                    degrees[neighbor]--;
                    if( degrees[neighbor]==1 )
                        myQue.push(neighbor);
                }
            }
        }
        return res;
    }
};
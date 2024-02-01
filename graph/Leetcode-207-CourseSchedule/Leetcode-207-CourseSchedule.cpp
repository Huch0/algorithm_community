class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> incomingEdgeCount(numCourses, 0);
        vector<vector<int>> edges(numCourses);
        
        for(vector<int>& pre : prerequisites){
            incomingEdgeCount[pre[0]]++;
            edges[pre[1]].push_back(pre[0]);
        }
        
        queue<int> noIncomingEdges;
        for(int i = 0; i < numCourses; i++){
            if(incomingEdgeCount[i] == 0){
                noIncomingEdges.push(i);
            }
        }
        
        int remainingEdgeCount = prerequisites.size();
        while(!noIncomingEdges.empty()){
            int cur = noIncomingEdges.front(); noIncomingEdges.pop();
            for(int nei : edges[cur]){
                remainingEdgeCount--;
                if(--incomingEdgeCount[nei] == 0){
                    noIncomingEdges.push(nei);
                }
            }
        }
        return remainingEdgeCount == 0;
    }
};
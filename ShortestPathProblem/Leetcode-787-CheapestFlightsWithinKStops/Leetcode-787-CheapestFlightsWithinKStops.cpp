class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<pair<int, int>>> edges(n);
        for(vector<int>& flight : flights){
            edges[flight[0]].emplace_back(flight[1], flight[2]);
        }
        
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<int> cur;
        int curCost, curSrc, curK;

        pq.push({0, src, K+1});
        
        while(!pq.empty()){
            cur = pq.top(); pq.pop();
            curCost = cur[0]; curSrc = cur[1]; curK = cur[2];
            if(curSrc == dst){
                return curCost;
            }
            if(curK > 0){
                for(pair<int, int>& nei : edges[curSrc]){
                    pq.push({curCost+nei.second, nei.first, curK-1});
                }
            }
        }
        
        return -1;
    }
};
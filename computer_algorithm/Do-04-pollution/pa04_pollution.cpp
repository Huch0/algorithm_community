#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<pair<int, int>, int> edge;
vector<edge> graph;
vector<int> polluted;
int counter = 0;

void printNextPollution() {
    vector<edge*> nextEdges;
    for (int i=0; i<graph.size(); i++) {
        if( graph[i].second == 0 ) continue;
        if( count(polluted.begin(), polluted.end(), graph[i].first.first) + count(polluted.begin(), polluted.end(), graph[i].first.second) == 1 ) {
            nextEdges.push_back(&graph[i]);
        }
    }

    int minCost = (*min_element(nextEdges.begin(), nextEdges.end(), [](edge* a, edge* b) {return a->second < b->second;}))->second;

    for_each(nextEdges.begin(), nextEdges.end(), [minCost](edge* e) {e->second -= minCost;});
    priority_queue<int, vector<int>, greater<int>> pq;
    for (auto e: nextEdges) {
        if( e->second == 0 ) {
            if( count(polluted.begin(), polluted.end(), e->first.first) == 0 ) pq.push(e->first.first);
            else pq.push(e->first.second);
        }
    }
    int toAdd = 0;
    while (!pq.empty()) {
        if( toAdd == pq.top() ) {
            pq.pop();
            continue;
        }
        toAdd = pq.top();
        pq.pop();
        cout << toAdd << endl;
        counter++;
        polluted.push_back(toAdd);
    }
}

int main() {
    int N, c1, c2; cin >> N >> c1 >> c2;

    for (int i=0; i<N-1; i++) {
        int a, b, c; cin >> a >> b >> c;
        graph.push_back({{a, b}, c});
    }

    polluted.push_back(c1); polluted.push_back(c2);

    while (counter < N-2) {
        printNextPollution();
    }

    return 0;
}
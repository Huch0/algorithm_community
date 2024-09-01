#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    int N; cin >> N;
    vector<pair<int, int>> meetings;
    for (int i=0; i<N; i++) {
        int start, end; cin >> start >> end;
        meetings.push_back(make_pair(end, start));
    }
    sort(meetings.begin(), meetings.end());
    int count = 0;
    int end = 0;
    for (int i=0; i<N; i++) {
        if( meetings[i].second >= end ) {
            end = meetings[i].first;
            count++;
        }
    }
    cout << count << endl;
}
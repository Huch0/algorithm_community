#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int N; cin >> N;
    vector<pair<int, int>> lines;
    for (int i=0; i<N; i++) {
        int a, b; cin >> a >> b;
        lines.push_back({a, b});
    }
    sort(lines.begin(), lines.end());
    int start = lines[0].first;

    int head = lines[0].first;
    int tail = lines[0].second;
    int total = 0;
    for (int i=0; i<N; i++) {
        if( lines[i].first < tail ) {
            if( lines[i].second > tail ) tail = lines[i].second;
        }
        else {
            total += tail - head;
            head = lines[i].first;
            tail = lines[i].second;
        }
    }
    total += tail - head;
    cout << total << endl;
}
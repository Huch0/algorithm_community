#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int N;
int minDiff = 2000000000;

int getDiff(vector<vector<int>>& synerges, vector<int>& selected) {
    vector<int> unselected;
    for (int i=0; i<N; i++)
        if( find(selected.begin(), selected.end(), i) == selected.end() ) unselected.push_back(i);

    int team1 = 0;
    int team2 = 0;
    for (int i=0; i<N/2; i++) {
        for (int j=0; j<N/2; j++) {
            if( i == j ) continue;
            team1 += synerges[selected[i]][selected[j]];
            team2 += synerges[unselected[i]][unselected[j]];
        }
    }
    //cout << team1 << ' ' << team2 << '\n';

    return abs(team1 - team2);
}
void backtracking(vector<vector<int>>& synerges, vector<int>& selected) {
    if( selected.size() == N/2 ) {
        int diff = getDiff(synerges, selected);
        minDiff = (diff < minDiff) ? diff : minDiff;
        //cout << N/2 << ' ' << selected.size() << ' ' << diff << ' ' << minDiff << '\n';
        return;
    }

    for (int i=0; i<N; i++) {
        if( selected.empty() || selected.back() < i ) {
            selected.push_back(i);
            backtracking(synerges, selected);
            selected.pop_back();
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    vector<vector<int>> synerges(N, vector<int>(N));

    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            cin >> synerges[i][j];
    
    vector<int> selected;

    for (int i=0; i<N/2; i++) {
        selected.push_back(i);
        backtracking(synerges, selected);
        selected.pop_back();
    }

    cout << minDiff << '\n';
}
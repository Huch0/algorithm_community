#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void backtracking(int N, int M, vector<int> v) {
    if( v.size() == M ) {
        for (int i=0; i<M; i++) cout << v[i] << ' ';
        cout << '\n';
        return;
    }

    for (int i=1; i<=N; i++) {
        if( find(v.begin(), v.end(), i) == v.end() ) {
            v.push_back(i);
            backtracking(N, M, v);
            v.pop_back();
        }
    }

}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M; cin >> N >> M;

    vector<int> v;

    backtracking(N, M, v);
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> v;
void backtracking() {
    if( v.size() == M ) {
        for (int i=0; i<M; i++) cout << v[i] << ' ';
        cout << '\n';
        return;
    }

    for (int i=1; i<=N; i++) {
        if( v.empty() || v.back() < i ) {
            v.push_back(i);
            backtracking();
            v.pop_back();
        }
    }

}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> N >> M;

    backtracking();
}
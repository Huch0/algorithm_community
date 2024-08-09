#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int result = 0;
vector<int> col;

bool promising(int idx) {
    for (int i=1; i<idx; i++)
        if( col[idx] == col[i] || abs(col[idx]-col[i]) == idx-i ) return false;
    return true;
}
void queens(int idx) {
    if( promising(idx) ) {
        if( idx == N ) result++;
        else {
            for (int i=1; i<=N; i++) {
                col[idx+1] = i;
                queens(idx+1);
            }
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    col.resize(N+1);

    queens(0);

    cout << result;
}
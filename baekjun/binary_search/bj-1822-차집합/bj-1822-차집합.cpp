#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, M; cin >> N >> M;
    vector<int> A(N), B(M);

    for (int i=0; i<N; i++) cin >> A[i];
    for (int i=0; i<M; i++) cin >> B[i];
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    vector<int> result;
    for (int i=0; i<N; i++)
        if( !binary_search(B.begin(), B.end(), A[i]) ) result.push_back(A[i]);
    
    if( result.empty() ) cout << 0;
    else {
        cout << result.size() << '\n';
        for (int r : result) cout << r << " ";
    }
}
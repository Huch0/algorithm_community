#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N; cin >> N;
    vector<int> v(N);
    for (int i=0; i<N; i++) cin >> v[i];

    sort(v.begin(), v.end());

    int M; cin >> M;
    vector<int> toFind(M);
    for (int i=0; i<M; i++) cin >> toFind[i];

    for (int i=0; i<M; i++) cout << binary_search(v.begin(), v.end(), toFind[i]) << " ";
}
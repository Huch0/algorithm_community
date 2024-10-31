#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    vector<int> v;
    for (int i=0; i<N; i++) {
        int k; cin >> k;
        v.push_back(k);
    }
    sort(v.begin(), v.end());
    int M; cin >> M;
    vector<int> a(M);
    for (int i=0; i<M; i++) cin >> a[i];

    for (int i=0; i<M; i++) {
        cout << upper_bound(v.begin(), v.end(), a[i])-lower_bound(v.begin(), v.end(), a[i]) << ' ';
    }
    return 0;
}
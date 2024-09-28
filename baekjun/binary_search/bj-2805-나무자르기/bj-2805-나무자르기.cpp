#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M; cin >> N >> M;
    vector<int> v(N);
    for (int i=0; i<N; i++) cin >> v[i];

    int left = 1, right = *max_element(v.begin(), v.end());
    while (left <= right) {
        int mid = (left+right)/2;
        long long sum = 0;
        for (int i=0; i<N; i++)
            if( v[i] > mid ) sum += v[i]-mid;
        if( sum >= M ) left = mid+1;
        else right = mid-1;
    }
    cout << right;
}
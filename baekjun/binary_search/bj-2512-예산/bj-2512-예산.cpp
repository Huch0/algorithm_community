#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N; cin >> N;
    vector<ll> v(N);
    for (int i=0; i<N; i++) cin >> v[i];
    ll M; cin >> M;

    ll left = 1, right = *max_element(v.begin(), v.end());
    while (left <= right) {
        ll mid = (left+right)/2;
        ll sum = 0;
        for (int i=0; i<N; i++) {
            if( v[i] > mid ) sum += mid;
            else sum += v[i];
        }
        if( sum <= M ) left = mid+1;
        else right = mid-1;
    }

    cout << right << endl;
}
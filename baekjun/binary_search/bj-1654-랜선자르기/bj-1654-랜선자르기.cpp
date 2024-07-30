#include <iostream>
#include <vector>
#include <algorithm>
#define ll long long
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int K, N; cin >> K >> N;
    vector<ll> v(K);
    for (int i=0; i<K; i++) cin >> v[i];
    
    ll left = 1, right = *max_element(v.begin(), v.end());
    while (left <= right) {
        ll mid = (left+right)/2;
        ll cnt = 0;
        for (int i=0; i<K; i++) cnt += v[i]/mid;
        if( cnt >= N ) left = mid+1;
        else right = mid-1;
    }

    cout << right << endl;
}
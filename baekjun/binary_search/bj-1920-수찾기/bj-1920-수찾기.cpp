#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int N; cin >> N;
    vector<int> v;
    for (int i=0; i<N; i++) {
        int k; cin >> k;
        v.push_back(k);
    }
    sort(v.begin(), v.end());
    int M; cin >> M;
    vector<int> a(M);
    for (int i=0; i<M; i++) cin>>a[i];
    
    for (int i=0; i<M; i++) {
        bool flag = false;
        int s = 0; int e = N-1;
        while (s <= e) {
            if( v[(s+e)/2] < a[i] ) s = (s+e)/2+1;
            else if( v[(s+e)/2] > a[i] ) e = (s+e)/2-1;
            else {
                flag = true;
                break;
            }
        }
        if( flag ) cout << "1\n";
        else cout << "0\n";
    }
    return 0;
}
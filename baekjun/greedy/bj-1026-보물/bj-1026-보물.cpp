#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N; cin >> N;
    vector<int> v1, v2;
    for (int i=0; i<N; i++) {
        int k; cin >> k;
        v1.push_back(k);
    }
    for (int i=0; i<N; i++) {
        int k; cin >> k;
        v2.push_back(k);
    }
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end(), greater<int>());
    
    int sum = 0;
    for (int i=0; i<N; i++)
        sum += v1[i]*v2[i];

    cout << sum << endl;
}
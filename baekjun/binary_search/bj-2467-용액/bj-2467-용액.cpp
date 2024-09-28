#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N; cin >> N;
    vector<int> v(N);
    for (int i=0; i<N; i++) cin >> v[i];

    int left = 0, right = N-1;
    int minSum = 2000000000;
    pair<int, int> result;
    while (left < right) {
        int sum = v[left] + v[right];
        if( abs(sum) < minSum ) {
            minSum = abs(sum);
            result = make_pair(v[left], v[right]);
        }
        if( sum < 0 ) left++;
        else right--;
    }
    cout << result.first << " " << result.second;
}
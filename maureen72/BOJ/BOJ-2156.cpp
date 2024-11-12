#include <iostream>
#include <algorithm>
using namespace std;

int n;
int dp[10001] = {0, };
int arr[10001] = {0, };

int main(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> arr[i];
    dp[0] = 0;
    dp[1] = arr[1];
    dp[2] = arr[1] + arr[2];
    dp[2] = arr[1] + arr[2];

    for(int i = 3; i <= n; i++){
        dp[i] = max({dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1]});
    }

    cout << dp[n];

}

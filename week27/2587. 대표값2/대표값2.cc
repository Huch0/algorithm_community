#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int num[5];
    int total = 0;
     
    for(int i = 0; i < 5; i++){
        cin >> num[i];  
        total += num[i];
    }
    
    int avg = total / 5;
    sort(num, num + 5);
    
    cout << avg << "\n" << num[2];
    
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main(){
    int sum = 0;
    int min = 100;
    int tmp;
    for(int i = 0; i < 7; i++){
        cin >> tmp;
        if(tmp % 2 == 1){
            sum += tmp;
            if(min > tmp) min = tmp;  
        } 
    }
    if (sum == 0){
        cout << -1 << "\n";
        return 0;
    }
    
    cout << sum << "\n";
    cout << min << "\n";
    return 0;
}
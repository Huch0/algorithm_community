#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, x;
    cin >> N;
    cin >> x;

    int tmp;
    for(int i = 0; i < N; i++){
        cin >> tmp;
        if (tmp < x){
            cout << tmp << " ";  
        } 
    }
    
    
    return 0;
}
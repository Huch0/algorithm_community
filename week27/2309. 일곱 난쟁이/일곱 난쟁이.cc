#include <bits/stdc++.h>
using namespace std;

int main(){
    int heights[9];
    int sum = 0;
    
    for(int i = 0; i < 9; i++){
        cin >> heights[i];
        sum += heights[i];
    }
    
    for(int j = 0; j < 8; j++){
        for(int k = j+1; k < 9; k++){
            if((sum - heights[j] - heights[k]) == 100){
                heights[j] = 0;
                heights[k] = 0;
                sort(heights, heights + 9);
                for(int l = 2; l < 9; l++) cout << heights[l] << "\n";
                return 0;
            }
        }
    }
    return 0;    
}
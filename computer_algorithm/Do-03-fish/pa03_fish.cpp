#include <iostream>
#include <vector>
using namespace std;

bool isOne(vector<int> &row, int k) {
    int i = 0;
    while (row[i] == i+1) i++;
    if( row[i] > 0 ) return false;
    int temp = -row[i];
    while (i < temp-1) {
        if( row[i] != row[i+1]-1) return false;
        i++;
    }
    i++;
    while (i < k) {
        if( row[i] != i+1) return false;
        i++;
    }
    return true;
}

void switchFish(vector<int> &row, int i, int j) {
    for (int k=0; k<(j-i+1)/2; k++) {
        int temp = row[i+k];
        row[i+k] = -row[j-k];
        row[j-k] = -temp;
    }
    if( (j-i)%2 == 0) row[i+(j-i)/2] = -row[(i+j)/2];
}

void printSwitching(vector<int> &row, int k) {
    if( isOne(row, k) == true) {
        cout << "one" << endl;
        return;
    }
    int left = 0; int right = k-1;
    while (row[left] == left+1) left++;
    while (row[right] == right+1) right--;
    
    int temp = k-1;
    while (row[temp] != -(left+1) && left <= temp) temp--;
    if( left <= temp ) {
        switchFish(row, left, temp);
        if( isOne(row, k) ) {
            cout << "two" << endl;
            return;
        }
        switchFish(row, left, temp);
    }

    
    temp = 0;
    while (row[temp] != -(right+1) && temp <= right) temp++;
    if( temp <= right ) {
        switchFish(row, temp, right);
        if( isOne(row, k) ) {
            cout << "two" << endl;
            return;
        }
    }
    cout << "over" << endl;
    return ;
}

int main() {
    int k; cin >> k;

    vector<vector<int>> fish;

    for (int i=0; i<5; i++) {
        vector<int> temp;
        for (int j=0; j<k; j++) {
            int n; cin >> n;
            temp.push_back(n);
        }
        fish.push_back(temp);
    }

    for (int i=0; i<5; i++) {
        printSwitching(fish[i], k);
    }

    return 0;
}
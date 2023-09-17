#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> v;
    int n = 1;
    while(n > 0){
        cin >> n;
        v.push_back(n);
    }
    int inputSize = v.size();

    int interval = 0;
    int xIntervals[inputSize/2];
    int yIntervals[inputSize/2];

    for(int i = 0; i < inputSize/2; i++){
        interval += v[i*2];
        xIntervals[i] = interval;
    }
    interval = 0;
    
    for(int i = inputSize/2-1; i >= 0; i--){
        interval += v[i*2+1];
        yIntervals[i] = interval;
    }

    int width = xIntervals[inputSize/2-1];
    int height = yIntervals[0];

    int x, y;

    while(cin >> x >> y){

        if(x > width || y > height){
            cout << "out" << endl;
            continue;
        }

        for(int i=0; i<inputSize/2; i++){
            if(x < xIntervals[i]){
                if(y < yIntervals[i]){
                    cout << "in" << endl;
                    break;
                }
                else if(y == yIntervals[i]){
                    cout << "on" << endl;
                    break;
                }
                else{
                    cout << "out" << endl;
                    break;
                }
            }
            else if(x == xIntervals[i] && i != inputSize/2-1){
                if(y < yIntervals[i+1]){
                    cout << "in" << endl;
                    break;
                }
                else if(y > yIntervals[i]){
                    cout << "out" << endl;
                    break;
                }
                else{
                    cout << "on" << endl;
                    break;
                }
            }
            else if(x == xIntervals[i] && i == inputSize/2-1){
                if(y > yIntervals[i]){
                    cout << "out" << endl;
                    break;
                }
                else{
                    cout << "on" << endl;
                    break;
                }
            }
        }
    }

    return 0;
}
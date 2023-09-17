#include <iostream>
#include <vector>
using namespace std;
#define TIME_INPUT 5
int main(){
    int size;
    cin >> size;

    struct Point{
        int x;
        int y;
    };
    vector<Point> points(size);
    
    for(int i=0; i<size; i++){
        cin >> points[i].x >> points[i].y;
    }

    vector<bool> signs(size); // true if negative(left or down), false if positive(right or up)
    vector<int> prefixIntervals(size+1);
    prefixIntervals[0] = 0;

    bool isVertical = (points[0].x == points[1].x) ? true : false;
    
    for(int i=0; i<size; i++){
        int interval;
        if(i == size-1) interval = isVertical ? points[0].y - points[i].y : points[0].x - points[i].x;
        else interval = isVertical ? points[i+1].y - points[i].y : points[i+1].x - points[i].x;
        if(interval < 0){
            signs[i] = true;
            interval *= -1;
        }
        else signs[i] = false;
        prefixIntervals[i+1] = prefixIntervals[i] + interval;
        isVertical = !isVertical;
    }

    vector<int> timePoints(TIME_INPUT);
    for(int& timePoint : timePoints) cin >> timePoint;

    for(int timePoint : timePoints){
        timePoint %= prefixIntervals[size];

        int targetIndex = 0;
        for(int i=0; i<size; i++){
            if(timePoint < prefixIntervals[i+1]){
                targetIndex = i;
                break;
            }
        }

        int offset = timePoint - prefixIntervals[targetIndex];
        if(signs[targetIndex]) offset *= -1;
        
        if( points[targetIndex].x == points[targetIndex+1].x ) cout << points[targetIndex].x << ' ' << points[targetIndex].y + offset << endl;
        else cout << points[targetIndex].x + offset << ' ' << points[targetIndex].y << endl;
    }

    return 0;
}
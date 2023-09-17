#include <iostream>
#include <vector>
using namespace std;

struct Point{
    int x;
    int y;
};

void getCopPoint(Point& targetCop, int reducedTimePoint, int initialCopInterval, vector<Point>& points, vector<bool>& signs, vector<int>& prefixIntervals){
    int targetIndex = 0;
    for(int i=0; i<points.size(); i++){
        if(reducedTimePoint < prefixIntervals[i+1]){
            targetIndex = i;
            break;
        }
    }

    int offset = reducedTimePoint - prefixIntervals[targetIndex];
    if(signs[targetIndex]) offset *= -1;
    if( points[targetIndex].x == points[targetIndex+1].x ) targetCop = {points[targetIndex].x, points[targetIndex].y + offset};
    else targetCop = {points[targetIndex].x + offset, points[targetIndex].y};
}

int main(){
    int size;
    cin >> size;

    vector<Point> points(size);
    
    for(int i=0; i<size; i++){
        cin >> points[i].x >> points[i].y;
    }

    vector<bool> signs(size);
    vector<int> prefixIntervals(size+1);
    prefixIntervals[0] = 0;

    bool isVertical = (points[0].x == points[1].x) ? true : false; // true if vertical, false if horizontal
    
    for(int i=0; i<size; i++){
        int interval;
        if(i == size-1) interval = isVertical ? points[0].y - points[i].y : points[0].x - points[i].x;
        else interval = isVertical ? points[i+1].y - points[i].y : points[i+1].x - points[i].x;
        if(interval < 0){
            signs[i] = true;
            interval *= -1; // absolute value
        }
        else signs[i] = false;
        prefixIntervals[i+1] = prefixIntervals[i] + interval;
        isVertical = !isVertical;
    }

    Point firstCop;
    Point secondCop;

    int timePoint;
    cin >> timePoint;

    int initialCopInterval = prefixIntervals[size/2-1]; // interval of the cop at the beginning

    int reducedTimePoint = timePoint % prefixIntervals[size]; //first cop's time point
    getCopPoint(firstCop, reducedTimePoint, initialCopInterval, points, signs, prefixIntervals);


    reducedTimePoint = (prefixIntervals[size] + initialCopInterval - reducedTimePoint) % prefixIntervals[size]; //second cop's time point
    getCopPoint(secondCop, reducedTimePoint, initialCopInterval, points, signs, prefixIntervals);


    int switchCounter = (timePoint-initialCopInterval/2-1) / (prefixIntervals[size]/2); // counting crossings
    if( switchCounter % 2 == 0 && timePoint > (initialCopInterval/2) ){
        Point temp = firstCop;
        firstCop = secondCop;
        secondCop = temp;
    }

    cout << firstCop.x << ' ' << firstCop.y << endl;
    cout << secondCop.x << ' ' << secondCop.y << endl;


    return 0;
}
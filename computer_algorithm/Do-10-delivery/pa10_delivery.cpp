#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> delivery;
vector<int> visited;
int minDist = 10000000;
vector<int> minPath;

int getMD(pair<int, int> a, pair<int, int> b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

bool isPossible(int temp, int i, int prev) {
    if( i%2 == 0 ) {
        if( count_if(visited.begin(), visited.end(), [](int a) { return a%2==0; }) - count_if(visited.begin(), visited.end(), [](int a) { return a%2==1; }) == 2 ) return false;
        return (find(visited.begin(), visited.end(), i) == visited.end());
    }
    else {
        if( find(visited.begin(), visited.end(), i) != visited.end() ) return false;
        if( find(visited.begin(), visited.end(), i-1) == visited.end() ) return false;
        if( getMD(delivery[i], delivery[prev]) + temp > minDist ) return false;
        return true;
    }
}

void dfs(int temp) {
    if( visited.size() == delivery.size() ) {
        if( minDist >= temp ) {
            bool change = true;
            if( minDist == temp ) {
                for (int i=0; i<visited.size(); i++) {
                    if( visited[i]%2 == 0) {
                        if( minPath[i] > visited[i] ) break;
                        else if( minPath[i] < visited[i] ) {
                            change = false;
                            break;
                        }
                    }
                    else {
                        if( minPath[i] > visited[i] ) {
                            change = false;
                            break;
                        }
                        else if( minPath[i] < visited[i] ) break;
                    
                    }
                }
            }
            minDist = temp;
            if( change ) minPath = visited;
        }
        return;
    }
    if( visited.empty() ) {
        for (int i=0; i<delivery.size(); i+=2) {
            visited.push_back(i);
            pair<int, int> p = make_pair(500, 500);
            dfs(getMD(p, delivery[i]));
            visited.pop_back();
        }
        return;
    }
    int prev = visited.back();
    for (int i=0; i<delivery.size(); i++) {
        if( isPossible(temp, i, prev) ) {
            visited.push_back(i);
            dfs(temp + getMD(delivery[i], delivery[prev]));
            visited.pop_back();
        }
    }
}

int main() {
    int n; cin >> n;
    for (int i=0; i<n; i++) {
        int a, b, c, d; cin >> a >> b >> c >> d;
        delivery.push_back({a, b});
        delivery.push_back({c, d});
    }
    dfs(0);

    for (int i=0; i<minPath.size(); i++) {
        if( minPath[i]%2 == 0 ) minPath[i] = minPath[i]/2+1;
        else minPath[i] = -(minPath[i]-1)/2-1;
    }

    for (auto i : minPath) {
        cout << i;
        if( i != minPath.back() ) cout << " ";
    }
    cout << endl;
    cout << minDist;
}
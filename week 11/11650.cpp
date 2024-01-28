#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <utility>
#include <vector>
#include <array>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.first == b.first) {
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main() {
    int N;
    cin >> N;
    vector <pair<int, int>> coordinates;
    pair<int, int> temp;
    int a;
    int b;
    while (N) {
        N--;
        cin >> a;
        cin >> b;
        temp = make_pair(a, b);
        coordinates.push_back(temp);
    }

    sort(coordinates.begin(), coordinates.end(),compare);
    for (pair<int, int> elements : coordinates) {
        cout << elements.first << " " << elements.second << "\n";
    }
    cin >> N;
}
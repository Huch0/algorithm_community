#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define SENTINEL 21
using namespace std;

int N, k, counterSize;
queue<pair<int, int>> carts;
vector<pair<int, int>> counters;
queue<int> payers;

void inputQueue() {
    for (int i = 0; i < N; i++) {
        int num; int cartSize;
        cin >> num >> cartSize;
        carts.push(make_pair(num, cartSize));
    }
}

void fillCounter() {
    while (counterSize != 0 && !carts.empty()) {
        auto it = find(counters.begin(), counters.end(), make_pair(0, SENTINEL));
        *it = carts.front();
        carts.pop();
        counterSize--;
    }
}

void outputQueue() {
    while (!carts.empty() || counterSize != k) {
        fillCounter();
        int minVal = min_element(counters.begin(), counters.end(), [](auto& k1, auto& k2){ return k1.second < k2.second; })->second;
        for_each(counters.begin(), counters.end(), [minVal](auto& k){ if (k.second != SENTINEL) k.second -= minVal; });
        for (auto rIt=counters.rbegin(); rIt != counters.rend(); rIt++) {
            if (rIt->second == 0) {
                payers.push(rIt->first);
                *rIt = make_pair(0, SENTINEL);
                counterSize++;
            }
        }
    }
}
void printPayers() {
    while (!payers.empty()) {
        cout << payers.front() << endl;
        payers.pop();
    }
}
int main() {
    cin >> N >> k;
    counterSize = k;
    counters.resize(k, make_pair(0, SENTINEL));

    inputQueue();
    outputQueue();
    printPayers();

    return 0;
}
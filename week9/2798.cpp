#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
    int N;
    int goal;
    cin >> N;
    cin >> goal;
    int i;
    int temp;
    vector<int> cards;
    for (i = 0;i < N;i++) {
        cin >> temp;
        cards.push_back(temp);
    }

    int sum=0;
    int best=0;
    for (i = 0;i < N - 2;i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N ;k++) {
                sum = cards[i] + cards[j] + cards[k];
                if (goal - sum < goal-best && sum<goal) {
                    best = sum;
                }
            }
        }
    }
    cout << best;
    cin >> N;
}
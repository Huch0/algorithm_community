#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int main() {
    int n;
    int temp;
    cin >> n;
    vector<int> numbers;
    for (int i = 0; i < n;i++) {
        cin >> temp;
        numbers.push_back(temp);
    }
    sort(numbers.begin(), numbers.end());
    for (int number : numbers) {
        cout << number << '\n';
    }
}
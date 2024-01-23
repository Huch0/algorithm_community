#include <iostream>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <utility>
#include <vector>

using namespace std;

bool compare(pair<int, string> a, pair<int, string> b)
{
    return a.first < b.first;
}

int main() {
    int N;
    vector<pair<int, string>> users;
    int temp_int;
    string temp_string;
    cin >> N;

    while (N) {
        N--;
        cin >> temp_int >> temp_string;
        users.push_back(make_pair(temp_int, temp_string));
    }

    stable_sort(users.begin(), users.end(), compare);

   

    for (const auto& pair : users) {
        cout << pair.first << " " << pair.second << '\n';
    }
    cin >> N;
}
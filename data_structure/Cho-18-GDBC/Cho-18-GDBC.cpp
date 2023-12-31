#include <iostream>
#include <unordered_map>
#include <set>
#include <queue>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

namespace std {
    template <>
    struct hash<set<int>> {
        size_t operator()(const set<int>& s) const {
            size_t hash_value = 0;
            for (const auto& elem : s) {
                hash_value ^= hash<int>()(elem) + 0x9e3779b9 + (hash_value << 6) + (hash_value >> 2);
            }
            return hash_value;
        }
    };
}
unordered_map<set<int>, vector<int>> GDBC;

void registerMode() {
    int id; cin >> id;
    set<int> idSet;
    while (id > 0) {
        idSet.insert(id);
        cin >> id;
    }
    
    GDBC[idSet].push_back(id);
    sort(GDBC[idSet].begin(), GDBC[idSet].end(), greater<int>());
}

void questionMode() {
    int id; cin >> id;
    set<int> idSet;
    while (id != 0) {
        idSet.insert(id);
        cin >> id;
    }
    if( GDBC.find(idSet) != GDBC.end() ) {
        for( int i = 0; i < GDBC[idSet].size(); i++ ) {
            cout << GDBC[idSet][i];
            if( i != GDBC[idSet].size() - 1 ) cout << " ";
        }
        cout << endl;
    }
    else cout << "None" << endl;
}

int main() {
    char op; cin >> op;
    while (op != '$') {
        if( op == 'R' ) registerMode();
        else if( op == 'Q' ) questionMode();
        else break;
        cin >> op;
    }
}
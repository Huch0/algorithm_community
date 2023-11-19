#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
using namespace std;

vector<vector<string>> mafia;

int getSize(string boss) {
    auto bossIt = find_if(mafia.begin(), mafia.end(), [boss](vector<string> v){return v.front() == boss;});
    if( bossIt->size() == 1 ) return 1;
    int size = 1;
    for (auto it = bossIt->begin()+1; it != bossIt->end(); it++) {
        size += getSize(*it);
    }

    return size;
}

int getRootDistance(string person) {
    int distance = 0;
    auto bossIt = find_if(mafia.begin(), mafia.end(), [person](vector<string> v){
        return find_if(v.begin()+1, v.end(), [person](string s){return s == person;}) != v.end();
    });
    if( bossIt == mafia.end() ) return 0;
    distance = getRootDistance(bossIt->front());
    distance++;

    return distance;
}

bool sortRules(tuple<string, int, int> a, tuple<string, int, int> b) {
    if( get<1>(a) > get<1>(b) ) return true;
    else if( get<1>(a) ==  get<1>(b) ) {
        if( get<2>(a) < get<2>(b)) return true;
        else if( get<2>(a) == get<2>(b) ) {
            return get<0>(a) < get<0>(b);
        }
    }

    return false;
}

void inputMafia() {
    int N; cin >> N;
    mafia.resize(N);
    auto it = mafia.begin();
    for (int i = 0; i < N-1; i++) {
        string person, boss;
        cin >> person >> boss;
        if( find_if(mafia.begin(), mafia.end(), [person](vector<string> v){return !v.empty() && v.front() == person;}) == mafia.end() ) {
            it->push_back(person);
            it++;
        }
        auto bossIt = find_if(mafia.begin(), mafia.end(), [boss](vector<string> v){return !v.empty() && v.front() == boss;});
        if( bossIt == mafia.end() ) {
            it->push_back(boss);
            bossIt = it;
            it++;
        }
        bossIt->push_back(person);
    }
}

void printSortedMafia() {
    vector<tuple<string, int, int>> bossVec;
    for (auto it = mafia.begin(); it != mafia.end(); ++it) {
        bossVec.push_back(make_tuple( it->front(), getSize(it->front()), getRootDistance(it->front()) ));
    }

    sort(bossVec.begin(),bossVec.end(), sortRules);

    for (auto t : bossVec) {
        cout << get<0>(t) << endl;
    }
}

int main() {
    inputMafia();

    printSortedMafia();

    return 0;
}
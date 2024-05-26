#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int k;
int mp, mf, ms, mv;
struct Ingredient {
    int p, f, s, v, c, idx;
};
vector<Ingredient> ingredients;
vector<vector<Ingredient>> leastSet;

bool isSatisfy(int p, int f, int s, int v) {
    if (p >= mp && f >= mf && s >= ms && v >= mv) return true;
    return false;
}

void findLeastSet() {
    int min = 300000;
    for (int i = 0; i < (1 << k); i++) {
        int p = 0, f = 0, s = 0, v = 0, c = 0;
        vector<Ingredient> temp;
        for (int j = 0; j < k; j++) {
            if (i & (1 << j)) {
                p += ingredients[j].p;
                f += ingredients[j].f;
                s += ingredients[j].s;
                v += ingredients[j].v;
                c += ingredients[j].c;
                temp.push_back(ingredients[j]);
            }
        }
        if (isSatisfy(p, f, s, v)) {
            if (c < min) {
                min = c;
                leastSet.clear();
                leastSet.push_back(temp);
            } else if (c == min) {
                leastSet.push_back(temp);
            }
        }
    }
}

int main() {
    cin >> k;
    cin >> mp >> mf >> ms >> mv;
    for (int i = 0; i < k; i++) {
        Ingredient toAdd; cin >> toAdd.p >> toAdd.f >> toAdd.s >> toAdd.v >> toAdd.c;
        toAdd.idx = i+1;
        ingredients.push_back(toAdd);
    }

    findLeastSet();

    if (leastSet.size() == 0) cout << 0;
    else {
        sort(leastSet.begin(), leastSet.end(), [](vector<Ingredient> a, vector<Ingredient> b) {
            int sumA = 0; int sumB = 0;
            for ( auto ingredient : a) {
                sumA += ingredient.p + ingredient.f + ingredient.s + ingredient.v;
            }
            for ( auto ingredient : b) {
                sumB += ingredient.p + ingredient.f + ingredient.s + ingredient.v;
            }

            if (sumA == sumB) {
                for (int i = 0; i < a.size(); i++) {
                    if (a[i].idx != b[i].idx) return a[i].idx < b[i].idx;
                }
            }
            return sumA > sumB;
        });
        for (auto ingredient : leastSet[0]) {
            cout << ingredient.idx << " ";
        }
    }
}
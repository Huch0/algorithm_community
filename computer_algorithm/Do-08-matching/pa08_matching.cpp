#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

int rk(string text, string pattern, int n, int m) {
    map<char, int> sigma;
    int sigma_size = 0;
    for (char c : text) {
        if( sigma.find(c) == sigma.end() ) sigma[c] = sigma_size++;
    }
    int q = 113;
    int d = sigma_size;
    int h = static_cast<int>(pow(d, m-1)) % q;
    int p = 0;
    int b = 0;
    for (int i = 0; i < m; i++) {
        p = (d*p + sigma[pattern[i]]) % q;
        b = (d*b + sigma[text[i]]) % q;
    }
    int count = 0;
    bool isMatch = false;
    for (int i = 0; i < (n-m+1); i++) {
        count ++;
        if( i != 0 ) {
            b = (d*(b - sigma[text[i-1]]*h) + sigma[text[i+m-1]]) % q;
            while (b < 0) b += q;
        }
        if( p == b ) {
            for (int j = 0; j < m; j++) {
                isMatch = true;
                count ++;
                if (pattern[j] != text[i+j]) {
                    isMatch = false;
                    break;
                }
            }
        }
        if( isMatch ) break;
    }

    return count;
}

void preprocessing(string pattern, vector<int>& sp, int m) {
    sp[0] = -1; int k = -1;
    for (int j=1; j<m; j++) {
        while ( k>=0 && pattern[j]!=pattern[k+1]) k = sp[k];
        if( pattern[j] == pattern[k+1] ) k++;
        sp[j] = k;
    }
}
int kmp(string text, string pattern, int n, int m) {
    vector<int> sp(m, 0);
    int count = 0;
    preprocessing(pattern, sp, m);
    int j = -1;

    for (int i=0; i<n; i++) {
        count ++;
        while (j>=0 && text[i]!=pattern[j+1]) {
            j = sp[j];
            count++;
        }
        if( text[i] == pattern[j+1] ) j++;
        if( j == m-1 ) {
            //j = sp[j];
            break;
        }
    }

    return count;
}

void computeSkip(string pattern, map<char, int>& jump, int m) {
    for (int i = 0; i < m; i++) {
        if( i != m-1 ) jump[pattern[i]] = m-i-1;
        if( i == m-1 && jump.find(pattern[i]) == jump.end() ) jump[pattern[i]] = m;
    }
    // for (auto it = jump.begin(); it != jump.end(); it++) {
    //     cout << it->first << " " << it->second << endl;
    // }
}
int bm(string text, string pattern, int n, int m) {
    map<char, int> jump;
    int count = 0;
    computeSkip(pattern, jump, m);
    int i = 0;
    while (i <= n-m) {
        count ++;
        int j = m-1;
        int k = i+m-1;
        while (j > 0 && pattern[j] == text[k]) {
            count ++;
            j--;
            k--;
        }
        if( j == 0 && pattern[j] == text[k] ) break;
        if( jump.find(text[i+m-1]) != jump.end() ) i += jump[text[i+m-1]];
        else i += m;
    }

    return count;
}
int main() {
    vector<pair<int, string>> algos(3);
    algos[0] = {0, "RK"};
    algos[1] = {0, "KMP"};
    algos[2] = {0, "BM"};

    int p; cin >> p;
    vector<string> patterns(p);
    for (int i = 0; i < p; i++) {
        string s; cin >> s;
        patterns[i] = s;
    }
    int t; cin >> t;
    vector<string> texts(t);
    for (int i = 0; i < t; i++) {
        string s; cin >> s;
        texts[i] = s;
    }

    for (int i = 0; i < p; i++) {
        for (int j = 0; j < t; j++) {
            int n = texts[j].size();
            int m = patterns[i].size();
            algos[0].first += rk(texts[j], patterns[i], n, m);
            algos[1].first += kmp(texts[j], patterns[i], n, m);
            algos[2].first += bm(texts[j], patterns[i], n, m);
        }
    }
    
    sort(algos.begin(), algos.end(), [](auto a, auto b) {return a.first < b.first;});
    
    if( algos[0].first == algos[1].first && algos[1].first == algos[2].first) cout << "0 0 0" << endl;
    else if( algos[0].first == algos[1].first) cout << "0 0 " << algos[2].second << endl;
    else if( algos[1].first == algos[2].first) cout << algos[0].second << " 0 0" << endl;
    else cout << algos[0].second << " " << algos[1].second << " " << algos[2].second << endl;

    //cout << algos[0].first << " " << algos[1].first << " " << algos[2].first << endl;

    // string s = "BFACF";
    // vector<int> qqq(5, 0);
    // preprocessing(s, qqq, 5);

    // for (int i = 0; i < 5; i++) {
    //     cout << qqq[i] << " ";
    // }

    return 0;
}
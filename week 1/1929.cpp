#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int m, n;

int main(void) {
    cin >> m >> n;
    int size = n - m + 1;
    int* prime = new int[n + 1];
    prime[1] = 0;
    for (int i = 2; i < n + 1; i++) {
        prime[i] = 1;
    }

    //eratostheneses sieve
    for (int i = 2; i < n + 1;i++) {
        if (prime[i] == 0) {
            continue;// continue, break
        }
        else {
            for (int j = i * 2; j < n + 1; j += i) { //you don't always have to incerase the index by 1
                prime[j] = 0;
            }
        }
    }


    for (int i = m; i < n + 1; i++) {
        if (prime[i] != 0) {
            cout << i << '\n'; //\n is faster than endl;
        }
    }

    //cin >> n;
    return 0;
}

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int P, N; cin >> P >> N;
    vector<int> schedule(N, P);

    int M; cin >> M;
    for (int i=0; i<M; i++) {
        int T; cin >> T;
        for (int j=0; j<T; j++) {
            int start, end, noise; cin >> start >> end >> noise;
            for (int k=start; k<end; k++) {
                schedule[k] += noise;
            }
        }
    }

    int max = 0;
    int temp = 0;
    for (int research : schedule) {
        temp += research;
        if( temp > max ) max = temp;
        if( temp < 0) temp = 0;
    }

    cout << max << endl;

    return 0;
}
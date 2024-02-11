#include <iostream>
#include <cstring>
#define p 1000000007
using namespace std;

int dptable[4000001];
int dptable2[4000001];

int fac(int n) {
	return dptable[n];
}

int pow(int a, int n) {
	int ans = 1;
	while(n) {
		if (n&1) ans = static_cast<long long>(ans) * a % p;
		a = static_cast<long long>(a) * a % p;
		n >>= 1;
	}
	return ans;
}

int ncr(int n, int r) {
	return (static_cast<long long>(dptable[n]) * dptable2[r] % p) * dptable2[n-r] % p;
}

int main() {
	memset(dptable, -1, sizeof(dptable));
	memset(dptable2, -1, sizeof(dptable2));
	dptable[0] = 1;
	dptable[1] = 1;
	for (int i=2; i<4000001; i++) {
		dptable[i] = static_cast<long long>(dptable[i-1]) * i % p;
	}
	dptable2[4000000] = pow(fac(4000000), p-2) % p; // 0!의 역원도 고려해줘야함 
	for (int i=3999999; i>=0; i--) {
		dptable2[i] = static_cast<long long>(dptable2[i+1]) * (i+1) %p;
	}

	int m, n, k;
	cin >> m;
	int array[m];

	for (int i=0; i<m; i++) {
		cin >> n >> k;
		array[i] = ncr(n,k);
	}
	//
    for (int i=0; i<30; i++) {
        int** ptr = new int*[500];
        for (int j=0; j<500; j++) {
            ptr[j] = new int[500];
            for (int k=0; k<500; k++) {
                ptr[j][k] = j+k;
            }
        }
        for (int j=0; j<500; j++) {
            delete[] ptr[j];
        }
        delete[] ptr;
    }
    //
	for (int i=0; i<m; i++) {
		cout << array[i] << "\n";
	}
}


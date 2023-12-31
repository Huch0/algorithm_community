#include <stdio.h>
int array[1000000] = {0, };
int main() {
	int m, n;
	scanf("%d %d", &m, &n);
	
	for (int i=2; i<=n; i++) {
		if (array[i] == 0) {
			if (i>=m) printf("%d\n", i);
			for (int j=i; j<=n; j+=i) {
				array[j] = 1;
			}
		}
	}
}

#include <stdio.h>
int main() {
	int n, k;
	int array[1001] = {0, };
	scanf("%d %d", &n, &k);
	
	int delcount = 0;
	int flag = 0;
	for (int i=2; i<=n; i++) {
		if (array[i] == 0) {
			for (int j=i; j<=n; j+=i) {
				if (array[j] == 0) {
					array[j] = 1;
					delcount++;
					if (delcount == k) {
						printf("%d", j);
						flag = 1;
					}
				}
			}
		}
		if (flag == 1) break;
	}
}

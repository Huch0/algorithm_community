#include <stdio.h>
#include <stdlib.h>

int count_distinct_values(int* values) {
	int i = 0;
	int len = 0;

	while (*(values + i) != -1) {
		i++;
		len++;
	}
	for (int p = 0; p < len; p++) {
		for (int k = 0; k < p; k++) {
			if (values[p] == values[k]) {
				i--;
				break;
			}
		}
	}
	return i;
}

#include <stdio.h>
#include <stdlib.h>

#define END_MARK	-1
#define MAX_SIZE	10000

int compare(const void* a, const void* b) {
	return (*(int*)b - *(int*)a);
}

int get_kth_largest(int* nums, int k) {

	int count = 0;
	while (nums[count] != END_MARK) {
		count++;
	}
	qsort(nums, count, sizeof(int), compare);

	return nums[k-1];
}

int main() {
	int nums[MAX_SIZE] = { 3, 7, 1, 5, 2, 4, END_MARK };
	int k = 3;

	int result = get_kth_largest(nums, k);

	printf("The %dth largest element is: %d\n", k, result);
	scanf("%d", &k);
	return 0;
}
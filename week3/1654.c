#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N, K, i, j;
	long long k_max = 0, max_len = 0, cnt;
	long long* list = NULL;
	scanf("%d %d", &K, &N);

	list = (long long*)calloc(K, sizeof(long long));

	for (i = 0; i < K; i++)
	{
		scanf(" %lld", &list[i]);
		if (list[i] > k_max) /*K개의 랜선 중 제일 큰애 찾기*/
			k_max = list[i];
	}

	long long left, mid, right;
	left = 1; right = k_max;

	while (left <= right)
	{
		mid = (left + right) / 2;

		for (j = 0, cnt = 0; j < K; j++)
		{
			cnt += list[j] / mid; /* 각 랜선마다 몇칸씩 나오는지 체크*/
		}

		if (N <= cnt && max_len < mid)
			max_len = mid;

		if (cnt < N)
			right = mid - 1;
		else
			left = mid + 1;

	}

	printf("%lld\n", max_len);

	return 0;
}
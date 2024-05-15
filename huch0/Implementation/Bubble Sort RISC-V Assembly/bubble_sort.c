#include <stdio.h>

void bubble_sort_2(int arr[], int n)
{
    int swap = 0;
    int no_swap = 0;
    for (int *last = &arr[n - 1]; last > &arr[0]; last--)
    {
        for (int *cur = &arr[0]; cur < last; cur++)
        {
            if (*cur > *(cur + 1))
            {
                int tmp = *cur;
                *cur = *(cur + 1);
                *(cur + 1) = tmp;
                swap++;
            }
            else
            {
                no_swap++;
            }
        }
    }

    printf("swap: %d\n", swap);
    printf("no_swap: %d\n", no_swap);
}

int main()
{
    int arr[] = {93, 3, 98, 31, 44, 89, 6, 2, 95, 15, 18, 22, 58, 92, 27, 10, 40, 32, 9, 47, 81, 12, 7, 74, 79, 5, 43, 78, 13, 70};
    int n = 30;

    bubble_sort_2(arr, n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
#include <iostream>
#include <vector>
/*
input :
- n : the number of elements in S
- S : a sorted array of n integers
output :
- x_index : the location of x in S; 0 if x is not in S.
*/
size_t interpolation_search(size_t n, std::vector<int> S, int x)
{
    size_t x_index, low, mid, high;

    low = 1;
    high = n;
    x_index = 0;
    if (S[low] <= x && x <= S[high])
    {
        while (low <= high && x_index == 0)
        {
            int denominator = S[high] - S[low];
            if (denominator == 0) // S[high] == S[low] == x
                mid = low;
            else
                mid = low + size_t((x - S[low]) * (high - low) / denominator);

            if (x == S[mid])
                x_index = mid; // x is at mid
            else if (x < S[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }
    }

    return x_index;
}

int main()
{
    size_t n = 10;
    std::vector<int> S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100};
    int x = 10;

    size_t x_index = interpolation_search(n, S, x);

    if (x_index == 0)
        std::cout << x << " is not in S." << std::endl;
    else
        std::cout << x << " is at " << x_index << " in S." << std::endl;

    return 0;
}
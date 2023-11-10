#include <iostream>
#include <algorithm>  // for sorting
using namespace std;
const int MAX_SIZE = 100000;

int binarySearch(int arr[], int low, int high, int target) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return 1;  // Element found
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return 0;  // Element not found
}

int main() {
    // Input the size of the first array
    int n;
    cin >> n;

    // Dynamic allocation of memory for the first array
    int* numbers = new int[n];

    // Input elements for the first array
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    // Sort the array (required for binary search)
    sort(numbers, numbers + n);

    // Input the size of the second array
    int m;
    cin >> m;

    // Input elements for the second array
    int* finding = new int[m];

    // Check if each element in the second array is present in the first array using binary search
    for (int i = 0; i < m; i++) {
        cin >> finding[i];
        cout << binarySearch(numbers, 0, n - 1, finding[i]) << endl;
    }

    // Deallocate dynamically allocated memory
    delete[] numbers;
    delete[] finding;

    return 0;
}

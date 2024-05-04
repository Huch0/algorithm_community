#include <iostream>
#include <vector>
using namespace std;

int getIndexByBinarysearch(int a, int b, vector<int> array, int n) {
	if (a>=b) {
		if (n > array[a]) return a+1;
		else return a;
	}
	if (array[(a+b)/2] < n) return getIndexByBinarysearch((a+b)/2+1, b, array, n);
	else return getIndexByBinarysearch(0, (a+b)/2-1, array, n);
}

int main() {
	int n;
	cin >> n;
	vector<int> array(n);
	for (int i=0; i<n; i++) {
		cin >> array[i];
	}
	for (int i=1; i<n; i++) {
		int target = array[i];
		int insertIndex = getIndexByBinarysearch(0, i, array, target);
		for (int j=i-1; j>=insertIndex; j--) array[j+1] = array[j];
		array[insertIndex] = target;
	}
	for (int i=0; i<n; i++) {
		cout << array[i] << endl;
	}
}

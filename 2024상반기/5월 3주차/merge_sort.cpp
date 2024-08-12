#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void merge(vector<int>& array, int a, int b) { // may be middle of array
	vector<int> tempv(b-a+1, 0);
	int m = (a+b)/2;
	int front = a, back = m+1, i;
	for (i=0; i<tempv.size(); i++) {
		if (front > m || back > b) break;
		if (array[front] <= array[back]) {
			tempv[i] = array[front];
			front++;
		}
		else {
			tempv[i] = array[back];
			back++;
		}
	}

	if (front > m) {
		for (; i<tempv.size(); i++) {
			tempv[i] = array[back];
			back++;
		}
	}
	else {
		for (; i<tempv.size(); i++) {
			tempv[i] = array[front];
			front++;
		}
	}
	copy(tempv.begin(), tempv.end(), array.begin()+a);
}
void mergesort(vector<int>& array, int a, int b) {
	if (a < b) {
		int m = (a+b)/2;
		mergesort(array, a, m);
		mergesort(array, m+1, b);
		merge(array, a, b);
	}
}

int main() {
	vector<int> array;
	int n;
	cin >> n;
	for (int i=0; i<n; i++) {
		int k;
		cin >> k;
		array.push_back(k);
	}
	
	mergesort(array, 0, n-1);
	
	for (int k : array) {
		cout << k << " ";
	}
}


#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;
void flip(vector<int> &array, int start, int end) {
	while(true) {
		if (start == end) {
			array[start] = -array[start];
			break;
		}
		else if (start > end) break;
		swap(array[start], array[end]);
		array[start] = -array[start];
		array[end] = -array[end];
		start++;
		end--;
	}
}
int isOne(vector<int> array) {
	int start, end, i;
	for (i=0; i<array.size(); i++) {
		if (array[i] != i+1) {
			start = i;
			break;
		}
	}
	for (i=array.size()-1; i>=0; i--) {
		if (array[i] != i+1) {
			end = i;
			break;
		}
	}
	flip(array, start, end);
	
	for (int i=0; i<array.size(); i++) {
		if (array[i] != i+1) return 0;
	}
	return 1;
}
int isTwo(vector<int> array) {
	vector<int> myarray(array);
	int start, end, i;
	
//case1 : ������ ����� �ذ�Ǵ� ��� ( ��� ������ �ٸ� ���ʿ� ���ԵǾ� �ִ� ���) 
	for (i=0; i<myarray.size(); i++) {
		if (myarray[i] != i+1) {
			start = i;
			break;
		}
	}
	for (i=myarray.size()-1; i>=0; i--) {
		if (myarray[i] != i+1) {
			end = i;
			break;
		}
	}
	flip(myarray, start, end);
	if (isOne(myarray)) return 1;
	
//case2 : ���� �������̾ ���� ������ ��� �ϴ� ��� 
	copy(array.begin(), array.end(), myarray.begin());
	for (i=0; i<myarray.size(); i++) {
		if (myarray[i] != i+1) {
			start = i;
			break;
		}
	}
	for (; i<myarray.size()-1; i++) {
		if (abs(myarray[i] - array[i+1]) != 1) {
			end = i; 
			break;
		}
	}
	flip(myarray, start, end);
	if (isOne(myarray)) return 1;
	
//case 3 : ���� ��迡 ���ļ� ������ ���
	copy(array.begin(), array.end(), myarray.begin());
	for (i=0; i<myarray.size(); i++) {
		if (myarray[i] != i+1) {
			start = i;
			break;
		}
	}
	for (; i<myarray.size()-1; i++) {
		if (abs(myarray[i] - array[i+1]) != 1) break;
	}
	i++;
	for (; i<myarray.size()-1; i++) {
		if (abs(myarray[i] - array[i+1]) != 1) {
			end = i;
			break;
		}
	}
	
	flip(myarray, start, end);
	if (isOne(myarray)) return 1;

//case 4 : ������ ��迡 ���ļ� ������ ���
	copy(array.begin(), array.end(), myarray.begin());
	for (i=myarray.size()-1; i>=0; i--) {
		if (myarray[i] != i+1) {
			end = i;
			break;
		}
	}
	for (; i>0; i--) {
		if (abs(myarray[i] - array[i-1]) != 1) break;
	}
	i--;
	for (; i>0; i--) {
		if (abs(myarray[i] - array[i-1]) != 1) {
			start = i;
			break;
		}
	}
	flip(myarray, start, end);
	if (isOne(myarray)) return 1;

	return 0;
}
int main() {
	int length;
	cin >> length;
	for (int i=0; i<5; i++) {
		vector<int> fishes(length);
		for (int i=0; i<length; i++) cin >> fishes[i];

		if (isOne(fishes)) cout << "one" << endl;
		else if (isTwo(fishes)) cout << "two" << endl;
		else cout << "over" << endl;
	}
}

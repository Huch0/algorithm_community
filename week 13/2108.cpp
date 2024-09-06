#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <math.h>
#include <queue>
using namespace std;

void Mean(vector<int>& nums, int size) {
	int mid = size / 2;
	if (size % 2 == 1) {
		cout << nums[mid] << endl;
	}
	else {
		int first = nums[mid - 1];
		first += nums[mid];
		first = first / 2;
		cout << first << endl;
	}
}


int main() {
	int n;
	int temp;
	vector <int> nums;
	cin >> n;
	while (n) {
		cin >> temp;
		nums.push_back(temp);
		n--;
	}
	int sum = 0;
	sort(nums.begin(), nums.end());

	for (int num : nums) {
		sum += num;
	}
	int avg=round((float)sum / nums.size());

	vector <int> count(8001,0);
	for (int num : nums) {
		count[num + 4000]++;
	}
	pair <int, int> first_index= make_pair(0,0);
	pair <int, int> second_index=make_pair(0,0);

	for (int i = 8000; i >=0;i--) {
		if (count[i] >= first_index.second) {
			second_index = first_index;
			first_index = make_pair(i, count[i]);
		}
	}
	//int mean= Mean(nums, nums.size())
	cout << avg<<endl;
	//cout << mean << endl;
	Mean(nums, nums.size());
	if (first_index.second == second_index.second) {
		cout << second_index.first-4000 << endl;
	}
	else {
		cout << first_index.first-4000 << endl;
	}
	cout << nums[nums.size() - 1] - nums[0]<<endl;
	cin >> n;
}

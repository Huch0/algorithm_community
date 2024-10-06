#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
/*
투포인터를 이용해서 정렬된 배열에서 두 수의 합이 특정 값이 되도록 / 특정 값에 가까워지도록 하는 두 수를 찾을 수 있다
typedef struct는 c언어의 문법임. C++은 그냥 struct로 만들면됌
emplace_back 사용법 
*/

//sol1 : 투포인터
/* 
int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	sort(a.begin(), a.end());
	
	int answer = 1000000001;
	for (int i=0; i<n; i++) {
		for (int j=i+3; j<n; j++) {
			int height = a[i] + a[j];
			int small = i+1, big = j-1;
			while (small != big) {
				answer = min(answer, abs(height - (a[small] + a[big])));
				if (answer == 0) {
					cout << 0;
					return 0;
				}
				else if (a[small] + a[big] < height) small++;
				else big--;
			}
		}
	}
	cout << answer;
}
*/

//sol2 : 가능한 눈사람 모두 만들기
struct snowman {
	int size;
	int i;
	int j;
	snowman (int _size, int _i, int _j) {
		size = _size;
		i = _i;
		j = _j;
	}
	bool operator < (snowman s) {
		return size < s.size;
	}
};
int main() {
	int n; cin >> n;
	vector<int> a(n);
	for (int i=0; i<n; i++) cin >> a[i];
	
	vector<snowman> snowmans;
	for (int i=0; i<n; i++) {
		for (int j=i+1; j<n; j++) {
			snowmans.emplace_back(a[i]+a[j], i, j);
		}
	}
	sort(snowmans.begin(), snowmans.end());
	
	int answer = 1000000001;
	for (int i=0; i<snowmans.size(); i++) {
		for (int j=i+1; j<snowmans.size(); j++) {
			if (snowmans[i].i == snowmans[j].i || snowmans[i].i == snowmans[j].j) continue;
			if (snowmans[i].j == snowmans[j].i || snowmans[i].j == snowmans[j].j) continue;
			answer = min(answer, abs(snowmans[i].size-snowmans[j].size));
			break;
		}
	}
	cout << answer;
}

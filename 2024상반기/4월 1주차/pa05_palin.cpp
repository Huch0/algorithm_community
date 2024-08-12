#include <iostream>
using namespace std;

int getPalinLength(string str) {
	int l = str.length();
	int lp, rp; // left pointer, right pointer
	int cutleft, cutright; // 자를 두 지점
	int cutlength = 100000; // 자를 길이
	for (int i=0; i<l/2; i++) {
		if (str[i] != str[l-1-i]) {
			if (i==0) return 0; // 회문이 아닌 경우 예외처리
			 
			//왼쪽 포인터를 오른쪽으로 옮겨가면서 어디를 지워야 할지 찾기.  
			lp = i;
			rp = l-1-i;
			while(lp != rp) { //왼쪽 포인터가 오른쪽에 닿을때까지 탐색. 중간에 찾으면 그냥 break.
				lp++;
				if (str[lp] == str[rp]) {
					int a = lp, b = rp;
					while(a < b) {
						if (str[a] != str[b]) break;
						a++;
						b--;
					}
					if (a >= b) { // 지우면 회문이 되는 적절한 경우를 찾은 것.
						cutleft = i;
						cutright = lp-1;
						cutlength = cutright - cutleft + 1;
						break;
					}
				}
			}
			
			//오른쪽 포인터를 왼쪽으로 옮겨가면서 어디를 지워야 할지 찾기.  
			lp = i;
			rp = l-1-i;
			while(lp != rp) {
				rp--;
				if (str[lp] == str[rp]) {
					int a = lp, b = rp;
					while(a < b) {
						if (str[a] != str[b]) break;
						a++;
						b--;
					}
					if (a >= b) {
						if ((l-1-i) - (rp+1) < cutlength) { // 왼쪽 포인터를 옮기면서 회문이 되는 경우와 비교해서 이게 더 나으면 바꿔준다 
							cutleft = rp + 1;
							cutright = l-1-i;
							cutlength = cutright - cutleft + 1;
							break;
						}
					}
				}
			}
			break;
		}
	}
	
	if (cutlength == 100000) return l;
	else return l - cutlength;
}

int main() {
	int n;
	cin >> n;
	for (int i=0; i<n; i++) {
		string str;
		cin >> str;
		cout << getPalinLength(str) << endl;
	}
}

#include <iostream>
using namespace std;

int getPalinLength(string str) {
	int l = str.length();
	int lp, rp; // left pointer, right pointer
	int cutleft, cutright; // �ڸ� �� ����
	int cutlength = 100000; // �ڸ� ����
	for (int i=0; i<l/2; i++) {
		if (str[i] != str[l-1-i]) {
			if (i==0) return 0; // ȸ���� �ƴ� ��� ����ó��
			 
			//���� �����͸� ���������� �Űܰ��鼭 ��� ������ ���� ã��.  
			lp = i;
			rp = l-1-i;
			while(lp != rp) { //���� �����Ͱ� �����ʿ� ���������� Ž��. �߰��� ã���� �׳� break.
				lp++;
				if (str[lp] == str[rp]) {
					int a = lp, b = rp;
					while(a < b) {
						if (str[a] != str[b]) break;
						a++;
						b--;
					}
					if (a >= b) { // ����� ȸ���� �Ǵ� ������ ��츦 ã�� ��.
						cutleft = i;
						cutright = lp-1;
						cutlength = cutright - cutleft + 1;
						break;
					}
				}
			}
			
			//������ �����͸� �������� �Űܰ��鼭 ��� ������ ���� ã��.  
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
						if ((l-1-i) - (rp+1) < cutlength) { // ���� �����͸� �ű�鼭 ȸ���� �Ǵ� ���� ���ؼ� �̰� �� ������ �ٲ��ش� 
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

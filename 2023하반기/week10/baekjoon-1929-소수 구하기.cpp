#include <stdio.h>
int main() {
	int a=86, b=320, c=77, d=92, e=133, answer = 0; // 100g´ç Ä®·Î¸®
	for (int i=0; i<2; i++) {
		int gram;
		char foodname;
		scanf("%c %d", &foodname, &gram);
		
		printf("foodname : %c", foodname);
		switch(foodname) {
			case 'A':
				answer += a*gram/100;
				printf(">>%d", answer);
				break;
			case 'B':
				answer += b*gram/100;
				printf(">>%d", answer);
				break;
			case 'C':
				answer += c*gram/100;
				printf(">>%d", answer);
				break;
			case 'D':
				answer += d*gram/100;
				printf(">>%d", answer);
				break;
			case 'E':
				answer += e*gram/100;
				printf(">>%d", answer);
				break;
		}
		printf("%d", answer);
	}
	printf("%d", answer);
}

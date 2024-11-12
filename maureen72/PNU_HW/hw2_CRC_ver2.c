#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define ZERO_PADDING 16 // 데이터워드 뒤에 붙는 0의 개수
#define DIVISOR_LENGTH 17 // divisor의 길이

void encoder(char* dataword, char* codeword, int K);
void decoder(char* codeword, char* output, int K);
void divide(char* dividend, char* divisor, char* remainder, int TOTAL_LENGTH);

int main() {
    int K; // dataword의 길이
    printf("Length of Dataword: ");
    scanf("%d", &K);

    int TOTAL_LENGTH = K + ZERO_PADDING; // codeword의 길이이

    char* dataword = (char*)malloc((K + 1) * sizeof(char));
    char* codeword = (char*)malloc((TOTAL_LENGTH + 1) * sizeof(char)); 
    char* output = (char*)malloc((K + 1) * sizeof(char));
    
    printf("Dataword(%d bit): ", K);
    scanf("%s", dataword);
    
    encoder(dataword, codeword, K);
    printf("Codeword: %s\n", codeword);
    
    printf("Codeword for decoder: ");
    scanf("%s", codeword);

    decoder(codeword, output, K);
    printf("codeword: %s\n", output);
    
    free(dataword);
    free(codeword);
    free(output);
    return 0;
}

void encoder(char* dataword, char* codeword, int K) {
    int TOTAL_LENGTH = K + ZERO_PADDING;
    char* A = (char*)malloc((TOTAL_LENGTH + 1) * sizeof(char)); // 데이터워드 + 16개의 0
    char remainder[DIVISOR_LENGTH] = {0}; // 나눗셈의 나머지
    char divisor[] = "10001000000100001";
    
    // 데이터워드에 16개의 0을 추가하여 A 생성
    snprintf(A, TOTAL_LENGTH + 1, "%s%016s", dataword, "");
    
    // A에 대해 나눗셈을 수행하고 나머지 저장
    divide(A, divisor, remainder, TOTAL_LENGTH);
    
    // 원래 데이터워드에 나머지를 추가하여 코드워드 생성
    snprintf(codeword, TOTAL_LENGTH + 1, "%s%s", dataword, remainder);

    // 나머지 값을 출력
    printf("remainder: %s\n", remainder);

    free(A);
}


void decoder(char* codeword, char* output, int K) {
    int TOTAL_LENGTH = K + ZERO_PADDING;
    char remainder[DIVISOR_LENGTH] = {0};
    char divisor[] = "10001000000100001";
    
    // 코드워드에 대해 나눗셈을 수행하고 나머지 저장
    divide(codeword, divisor, remainder, TOTAL_LENGTH);
    
    // 나머지가 모두 0인지 확인
    if (strcmp(remainder, "0000000000000000") == 0) {
        strncpy(output, codeword, K); // 모두 0이면 원래 데이터워드 반환
        output[K] = '\0'; // 널 종료 보장
    } else {
        strcpy(output, "Error"); // 그렇지 않으면 에러 메시지 반환
    }
}

void divide(char* dividend, char* divisor, char* remainder, int TOTAL_LENGTH) {
    int len = strlen(dividend);
    char* temp = (char*)malloc((TOTAL_LENGTH + 1) * sizeof(char));
    
    strncpy(temp, dividend, len);
    temp[len] = '\0';
    
    for (int i = 0; i <= len - DIVISOR_LENGTH; i++) {
        if (temp[i] == '1') {
            for (int j = 0; j < DIVISOR_LENGTH; j++) {
                temp[i + j] = (temp[i + j] == divisor[j] ? '0' : '1');
            }
        }
    }
    // 나머지를 나머지 배열에 복사
    strncpy(remainder, temp + len - DIVISOR_LENGTH + 1, DIVISOR_LENGTH - 1);
    remainder[DIVISOR_LENGTH - 1] = '\0'; // 널 종료 보장

    free(temp);
}
#include <stdio.h>

int main(){
    int order = 0;
    int largest = 0;
    for(int i = 0; i < 9; i++){
        int tmp = 0;
        scanf("%d", &tmp);
        if (tmp > largest){
            largest = tmp;
            order = i + 1;
        }
    }
    
    printf("%d\n%d", largest, order);

    return 0;
}
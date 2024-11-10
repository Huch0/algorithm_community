package algorithm;

import java.util.Scanner;

public class Baekjoon_11726_2xn타일링 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];

        array[0] = 1;
        if(n>1) array[1] = 2;

        for(int i = 2; i < n; i++){
            array[i] = (array[i-1] + array[i-2])%10007; // 계산을 다 하고 mod연산을 하면 오버플로우 문제 발생. 나눠서 배열에 넣어도 결과는 동일.
        }

        System.out.println(array[n-1]);
    }
}

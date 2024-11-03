package algorithm;

import java.math.BigInteger;
import java.util.Scanner;

public class Baekjoon_1914_하노이탑 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        BigInteger[] array = new BigInteger[n+1];   // n이 매우 클 경우 int,long 자료형을 사용하면 오버플로우 발생

        array[1] = new BigInteger("1");
        for(int i = 2; i < n+1; i++){
            array[i] = (array[i-1].multiply(BigInteger.valueOf(2)).add(BigInteger.valueOf(1)));
        }
        System.out.println(array[n]);
        if(n<=20){
            hanoi(n,0,2);
        }
    }

    static void hanoi(int n, int start, int end){
        if(n==1) {System.out.println((start+1) + " " + (end+1)); return;}
        hanoi(n-1,start, (6-start-end)%3);
        hanoi(1,start,end);
        hanoi(n-1,(6-start-end)%3,end);
    }
}

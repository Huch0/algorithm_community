package algorithm.DynamicProgramming;

import java.util.*;

public class Baekjoon_9461_파도반수열_BottomUp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        long[] array = new long[100];

        array[0] = 1; array[1] = 1; array[2] = 1; array[3] = 2; array[4] = 2;
        
        for(int i = 5; i < 100; i++){
            array[i] = array[i-1] + array[i-5];
        }

        for(int i = 0; i < n; i++){
            System.out.println(array[sc.nextInt()-1]);
            sc.nextLine();
        }
    }
}

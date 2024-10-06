package algorithm.DynamicProgramming;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Baekjoon_2579_계단오르기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = new int[n+1];
        int[] dp = new int [n+1];

        for(int i = 1; i < n+1; i++){
            array[i] = Integer.parseInt(br.readLine());
        }
        
        dp[0] = 0;
        dp[1] = array[1];
        if(n>=2) dp[2] = array[1] + array[2];

        for(int i = 3; i < n+1; i++){
            dp[i] = Math.max(dp[i-3] + array[i-1], dp[i-2]) + array[i];
        }
        System.out.println(dp[n]);
    }
} 

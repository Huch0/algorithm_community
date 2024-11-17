package algorithm.Greedy.Baekjoon_11047_동전0;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Baekjoon_11047_동전0 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] num = br.readLine().split(" ");
        int n = Integer.parseInt(num[0]);
        int total = Integer.parseInt(num[1]);
        int[] coin = new int[n];
        int result = 0;

        for(int i = 0; i < n; i++){
            coin[i] = Integer.parseInt(br.readLine());
        }

        while(total > 0){
            boolean flag = false;
            for(int i = 1; i < n; i++){
                if(coin[i] > total){
                    total -= coin[i-1];
                    result++;
                    flag = true;
                    break;
                }
            }
            if(!flag) {
                total -= coin[n-1];
                result++;
            }
        }
        System.out.println(result);
    }
}

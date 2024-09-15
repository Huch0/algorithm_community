package algorithm.Greedy.Leetcode_11399_ATM;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.Arrays;

public class Leetcode_11399_ATM {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];

        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(array);

        for(int i = 0; i < n-1; i++){
            array[i+1] = array[i] + array[i+1];
        }

        int sum = 0;
        for(int num : array){
            sum += num;
        }
        System.out.println(sum);
    }
}

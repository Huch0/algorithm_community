package algorithm.DynamicProgramming.Baekjoon_9095_123더하기;

import java.io.*;

public class Baekjoon_9095_123더하기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = new int[12];
        
        array[1] = 1;
        array[2] = 2;
        array[3] = 4;

        for(int i = 4; i < 12; i++){
            array[i] = array[i-1] + array[i-2] + array[i-3];
        }

        for(int i = 0; i < n; i++){
            System.out.println(array[Integer.parseInt(br.readLine())]);
        }
    }
}

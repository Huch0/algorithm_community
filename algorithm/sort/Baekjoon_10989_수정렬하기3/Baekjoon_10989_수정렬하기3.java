package algorithm.sort.Baekjoon_10989_수정렬하기3;

import java.util.*;
import java.io.*;

public class Baekjoon_10989_수정렬하기3 {
    public static void main(String[] args) throws IOException {
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(buffer.readLine());

        int[] array = new int[n];
        int[] count = new int[10001];
        int[] sortedArray = new int[n];

        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(buffer.readLine());
            array[i] = num;
            count[num] += 1;   
        }

        for(int i = 0; i < n; i++){
            count[i+1] = count[i] + count[i+1];
        }

        for(int i = 0; i < n; i++){
            count[array[i]] -= 1;
            sortedArray[count[array[i]]] = array[i];
        }
        
        for(int num : sortedArray){
            bw.write(num + "\n");
        }
        bw.flush();
    }
}

package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Baekjoon_18111_마인크래프트_bruteforce {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int minTime = 100000000;
        int maxBlock = 0;

        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());
        int block = Integer.parseInt(st.nextToken());

        int max = 0;
        int min = 256;

        int[][] array = new int[row][col];

        for(int i = 0; i < row; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < col; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
                max = max < array[i][j] ? array[i][j] : max;
                min = min > array[i][j] ? array[i][j] : min;
            }
        }
        
        for(int k = min; k <= max; k++){
            int needBlock= block;
            int time = 0;
            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    if(array[i][j] < k){
                        time += (k-array[i][j]);
                    }
                    else if(array[i][j] > k){
                        time += 2*(array[i][j]-k);
                    }
                    needBlock += array[i][j]-k;
                }
            }
            if(needBlock < 0) continue;
            
            if(minTime >= time){
                minTime = time;
                maxBlock = k;
            }
        }

        System.out.println(minTime + " " + maxBlock);
    }
}
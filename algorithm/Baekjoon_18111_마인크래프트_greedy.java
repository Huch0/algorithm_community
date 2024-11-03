package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Baekjoon_18111_마인크래프트_greedy {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int result = 0;

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
    
        while(max != min){ 
            int plus = 0;
            int sub = 0;

            for(int i = 0; i < row; i++){
                for(int j = 0; j < col; j++){
                    if(array[i][j] == max) {
                        sub++;
                    }
                    if(array[i][j] == min){
                        plus++;
                    }
                }
            }
                
            if(2*sub < plus){
                for(int i = 0; i < row; i++){
                    for(int j = 0; j < col; j++){
                        if(array[i][j] == max) {
                            array[i][j]--;
                        }
                    }
                }
                result += 2*sub;
                block += sub;
                max--;
            }
            else {
                if(block < plus) { 
                    for(int i = 0; i < row; i++){
                        for(int j = 0; j < col; j++){
                            if(array[i][j] == max) {
                                array[i][j]--;
                            }
                        }
                    }
                    result += 2*sub;
                    block += sub; 
                    max--; 
                    continue;
                }
                for(int i = 0; i < row; i++){
                    for(int j = 0; j < col; j++){
                        if(array[i][j] == min) {
                            array[i][j]++;
                        }
                    }
                }
                
                result += plus;
                block -= plus;
                min++;
            }
        }
        System.out.println(result + " " + max);

    }
}
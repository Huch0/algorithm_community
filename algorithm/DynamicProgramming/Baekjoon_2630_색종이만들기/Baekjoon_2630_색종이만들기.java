package algorithm.DynamicProgramming.Baekjoon_2630_색종이만들기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Baekjoon_2630_색종이만들기 {
    public static int blue;
    public static int white;
    public static int[][] array;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        array = new int[n][n];

        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        partition(n,0,0); 
        System.out.println(white);
        System.out.println(blue);
    }

    public static void partition(int size,int x,int y){
        if(isSameColor(size,x,y)){
            if(array[x][y] == 0) white++;
            else blue++;
            return;
        }
        partition(size/2,x,y);
        partition(size/2,x+size/2,y);
        partition(size/2,x,y+size/2);
        partition(size/2,x+size/2,y+size/2);

    }

    public static boolean isSameColor(int size, int x, int y){
        int color = array[x][y];
        for(int i =  x; i < x + size; i++) {
            for(int j = y; j < y + size; j++){
                if(color != array[i][j]) return false;
            }
        }
        return true;
    }
}

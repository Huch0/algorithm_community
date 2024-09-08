package algorithm.graph.DFS.Baekjoon_2667_단지번호붙이기;

import java.io.*;
import java.util.*;

public class Baekjoon_2667_단지번호붙이기 {
    static int count = 0;
    public static void main(String[] args)  throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine());
        String[] line;
        int[][] array = new int[n][n];

        for(int i = 0; i < n; i++){
            line = br.readLine().split("");
            for(int j =0; j < n; j++){
                array[i][j] = Integer.parseInt(line[j]);
            }
        }

        int total = 0;
        for(int i = 0; i < n; i++){
            for(int j =0; j < n; j++){
                if(array[i][j] == 1) {dfs(array,i,j); heap.add(count); count = 0; total++;} 
            }
        }
        
        System.out.println(total);
        while(!heap.isEmpty()){
            System.out.println(heap.poll());
        }
    }

    public static void dfs(int[][] array, int x, int y){
        if(x<0 || x>=array.length || y<0 || y>=array[0].length || array[x][y] == 0) { return; }

        array[x][y] = 0;
        count += 1;

        dfs(array, x+1, y);
        dfs(array, x-1, y);
        dfs(array, x, y+1);
        dfs(array, x, y-1);

        return;
    }
}

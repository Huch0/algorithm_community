package algorithm.graph.BFS.Baekjoon_14940_쉬운최단거리;

import java.io.*;
import java.util.*;

public class Baekjoon_14940_쉬운최단거리{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Queue<int[]> queue = new LinkedList<>();

        int totalRow = Integer.parseInt(st.nextToken());
        int totalCol = Integer.parseInt(st.nextToken());

        int startRow = 0;
        int startCol = 0;

        int[][] array = new int[totalRow][totalCol];

        for(int i = 0; i < totalRow; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < totalCol; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
                if(array[i][j] == 2) {startRow = i; startCol = j;}
            }
        }

        array[startRow][startCol] = 3;
        queue.add(new int[] {startRow+1,startCol,array[startRow][startCol]});
        queue.add(new int[] {startRow-1,startCol,array[startRow][startCol]});
        queue.add(new int[] {startRow,startCol+1,array[startRow][startCol]});
        queue.add(new int[] {startRow,startCol-1,array[startRow][startCol]});

        while(!queue.isEmpty()){
            int[] node = queue.poll();
            int row = node[0];
            int col = node[1];
            int prev = node[2];

            if(row < 0 || row >= array.length || col < 0 || col >= array[0].length || array[row][col] > 2 || array[row][col] == 0) {continue;}

            array[row][col] = prev + 1;
            queue.add(new int[] {row-1,col,array[row][col]});
            queue.add(new int[] {row+1,col,array[row][col]});
            queue.add(new int[] {row,col-1,array[row][col]});
            queue.add(new int[] {row,col+1,array[row][col]});
        }
        

        for(int i = 0; i < totalRow; i++){
            for(int j = 0; j < totalCol; j++){
                if(array[i][j] == 0) {continue;}
                else if(array[i][j] == 1) {array[i][j] = -1;}
                else {array[i][j] -= 3;}
            }
        }

        for(int i = 0; i < totalRow; i++){
            for(int j = 0; j < totalCol; j++){
                bw.write(Integer.toString(array[i][j])); bw.write(" ");
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}

package algorithm.DynamicProgramming.Baekjoon_1074_Z;

import java.util.Scanner;

public class Baekjoon_1074_Z_DivedandConquer {
    public static int result=0;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int row = sc.nextInt();
        int col =  sc.nextInt();
        partition(n,row,col);

        System.out.println(result);
    }

    public static void partition(int n, int row, int col){
        int size = (int)Math.pow(2,n);
        if(size != 2){
            if(row < size/2 && col < size/2) result += 0; 
            else if(row < size/2 && col >= size/2) {result += (int)Math.pow(4,n-1); col -= size/2;}
            else if(row >= size/2 && col < size/2) {result += (int)Math.pow(4,n-1)*2; row -= size/2;}
            else if(row >= size/2 && col >= size/2) {result += (int)Math.pow(4,n-1)*3; col -= size/2; row -= size/2;}
            partition(n-1, row, col);
        }
        else {
            if(row == 0 && col == 0) result += 0;
            else if(row == 0 && col == 1) result += 1;
            else if(row == 1 && col == 0) result += 2;
            else if(row ==1  && col == 1) result += 3;
            return;
        }
        return;
    }
}

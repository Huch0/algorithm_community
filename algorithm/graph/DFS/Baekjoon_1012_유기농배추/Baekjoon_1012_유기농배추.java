import java.util.*;

public class Baekjoon_1012_유기농배추 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < n; i++){
            int row = sc.nextInt();
            int col = sc.nextInt();
            int[][] field = new int[row][col];
            int k = sc.nextInt();
            sc.nextLine();

            for(int j = 0; j < k; j++){
                int x = sc.nextInt();
                int y = sc.nextInt();
                sc.nextLine();

                field[x][y] = 1;
            }

            int count = 0;

            for(int p = 0; p < row; p++){
                for(int q = 0; q < col; q++){
                    if(field[p][q] == 1) {dfs(field,p,q); count += 1;}
                }
            }

            System.out.println(count);
        }
    }

    public static void dfs(int[][] feild, int x, int y){
        if (x<0 || x >= feild.length || y < 0 || y >= feild[0].length) return;
        if(feild[x][y] == 0) return;
        else {
            feild[x][y] = 0;
            dfs(feild,x+1,y);
            dfs(feild,x-1,y);
            dfs(feild,x,y+1);
            dfs(feild,x,y-1);
        }
    }
}

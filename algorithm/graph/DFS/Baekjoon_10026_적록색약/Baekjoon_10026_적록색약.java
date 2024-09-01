import java.util.*;

public class Baekjoon_10026_적록색약 {
    public static void dfs(char[][] charArray, char c, int x, int y, boolean isColorWeakness){
        if(x < 0 || x >= charArray.length || y < 0 || y >= charArray.length || charArray[x][y] == 'X') 
            return;

        char now = charArray[x][y];
        if(isColorWeakness && (now == 'R' || now == 'G') && (c == 'R' || c == 'G')){
            charArray[x][y] = 'X';
            dfs(charArray, c, x+1, y, isColorWeakness);
            dfs(charArray, c, x-1, y, isColorWeakness);
            dfs(charArray, c, x, y+1, isColorWeakness);
            dfs(charArray, c, x, y-1, isColorWeakness);
        } else if(now == c){
            charArray[x][y] = 'X';
            dfs(charArray, c, x+1, y, isColorWeakness);
            dfs(charArray, c, x-1, y, isColorWeakness);
            dfs(charArray, c, x, y+1, isColorWeakness);
            dfs(charArray, c, x, y-1, isColorWeakness);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        char[][] charArray1 = new char[n][n];
        char[][] charArray2 = new char[n][n];
        String input;

        for(int i = 0; i < n; i++){
            input = sc.nextLine();
            for(int j = 0; j < n; j++){
                charArray1[i][j] = input.charAt(j);
                charArray2[i][j] = input.charAt(j);
            }
        }

        int commonCount = 0;
        int colorWeaknessCount = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(charArray1[i][j] != 'X') {
                    dfs(charArray1, charArray1[i][j], i, j, false);
                    commonCount++;
                }
                if(charArray2[i][j] != 'X') {
                    dfs(charArray2, charArray2[i][j], i, j, true);
                    colorWeaknessCount++;
                }
            }
        }

        System.out.println(commonCount + " " + colorWeaknessCount);
    }
}

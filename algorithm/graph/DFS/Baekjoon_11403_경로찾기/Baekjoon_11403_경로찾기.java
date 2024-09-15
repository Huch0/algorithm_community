package algorithm.graph.DFS.Baekjoon_11403_경로찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Arrays;

public class Baekjoon_11403_경로찾기 {
    static HashSet<Integer> visited = new HashSet<>();
    static HashMap<Integer,ArrayList<Integer>> result = new HashMap<>();
    static HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] temp;

        int n = Integer.parseInt(br.readLine());

        for(int i = 1; i < n+1; i++){
            temp = br.readLine().split(" ");
            map.put(i,new ArrayList<>());
            result.put(i, new ArrayList<>());
            for(int j = 0; j < n; j++){
                if(temp[j].equals("1")) map.get(i).add(j+1);
            }
        }

        for(int key : map.keySet()){
            for(int num : map.get(key)){
                dfs(key,num);
            }
            visited.clear();
        }

        int[][] resultArray = new int[n][n];
        for(int i = 0; i < n; i++) Arrays.fill(resultArray[i],0);
        
        for(int i : result.keySet()){
            for(int j : result.get(i)){
                resultArray[i-1][j-1] = 1; 
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.print(resultArray[i][j]); System.out.print(" ");
            }
            System.out.println();
        }

    }

    public static void dfs(int key, int value){ 
        if(visited.contains(value)) return;
        else{
            result.get(key).add(value);
            visited.add(value);
            for(int num : map.get(value)){
                dfs(key,num);
            }
        }
    }
}

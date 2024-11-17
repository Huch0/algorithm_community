package algorithm.BinarySearch.Baekjoon_10815_숫자카드;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Baekjoon_10815_숫자카드 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] haveArray = new int[n];
        for(int i = 0; i< n; i++){
            haveArray[i] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] searchArray = new int[m];
        for(int i = 0; i< m; i++){
            searchArray[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(haveArray);
        int[] result = new int[m];
        for(int i = 0; i < m; i++){
            int low = 0;
            int high = n-1;
            boolean flag = false;
            while(low <= high){
                int mid = (low+high)/2;
                if(haveArray[mid] == searchArray[i]) {result[i] = 1; flag = true; break;}
                else if(haveArray[mid] > searchArray[i]) {high = mid-1;}
                else {low = mid+1;}
            }
            if(!flag) {result[i] = 0;}
        }

        for(int num : result){
            System.out.print(num + " ");
        }
    }

}

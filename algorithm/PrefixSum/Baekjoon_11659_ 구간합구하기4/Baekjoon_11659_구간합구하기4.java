import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon_11659_구간합구하기4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int length = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);

        line = br.readLine().split(" ");
        int[] array = new int[length];
        int[] prefixSum = new int[length];
        for (int i = 0; i < length; i++) {
            array[i] = Integer.parseInt(line[i]);
            if(i==0) {prefixSum[i] = array[i];}
            else {prefixSum[i] = prefixSum[i-1] + array[i];}
        }
        
        int start = 0, end = 0;
        for(int i = 0; i < n; i++){
            line = br.readLine().split(" ");
            start = Integer.parseInt(line[0])-1;
            end = Integer.parseInt(line[1])-1;

            if(start == 0) {System.out.println(prefixSum[end]);}
            else {System.out.println(prefixSum[end]-prefixSum[start-1]);}
        }

    }


}

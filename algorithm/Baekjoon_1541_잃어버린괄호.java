package algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Baekjoon_1541_잃어버린괄호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] sumArray = br.readLine().split("-");
        int[] nums = new int[sumArray.length];

        for(int i = 0; i < sumArray.length; i++){
            String[] sum = sumArray[i].split("\\+");
            for(int j = 0; j < sum.length; j++){
                nums[i] += Integer.parseInt(sum[j]);
            }
        }

        int result = nums[0];
        for(int i = 1; i < nums.length; i++){
            result -= nums[i];
        }
        System.out.println(result);
    }
}

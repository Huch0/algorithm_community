package algorithm.sort.Baekjoon_2108_통계학;

import java.util.Arrays;
import java.util.Scanner;

public class Baekjoon_2108_통계학 {
    	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] array = new int[n];

		int average = 0;
		int middle = 0;
		int mostCommon = 0;
		int term = 0;
		
		for(int i = 0; i < n; i++) {
			array[i] = sc.nextInt();
			sc.nextLine();	
		}
        
        int[] sortedArray = new int[array.length];
		int[] count = new int[Arrays.stream(array).max().orElse(0)+1+4000];
		for(int num : array){
			count[num+4000] += 1;

		} 
		int maxCount = count[0];
		boolean flag = true;
		for(int i = 0; i < count.length-1; i++){
			if (count[i+1] > maxCount) {maxCount = count[i+1]; mostCommon = i+1-4000; flag = true;}
			else if (count[i+1] == maxCount && flag) {mostCommon = i+1-4000; flag = false;}
			count[i+1] = count[i]+count[i+1];
        }
		for(int i = array.length-1; i >= 0;i--){
			count[array[i]+4000]--;
			sortedArray[count[array[i]+4000]] = array[i];
		}

		average = (int)Math.round(Arrays.stream(array).sum()/(double)n);
		middle = sortedArray[n/2];

		term = sortedArray[array.length-1] - sortedArray[0];
		
		System.out.println(average);
		System.out.println(middle);
		System.out.println(mostCommon);
		System.out.println(term);
	}
}

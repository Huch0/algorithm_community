package algorithm.sort;

import java.util.*;

public class CountingSort {
	public static void main(String[] args) {
		int[] array = {0,3,5,8,41,4,5,9,4,5,3,1,5,8,7,9,5,1,6,8,7,5,23,4,21,14,54,34,23,12};
		for(int num : countingSort(array)){
			System.out.print(num); System.out.print(" ");
		}
	}

	public static int[] countingSort(int[] array) {
		int[] result = new int[array.length];
		int[] count = new int[Arrays.stream(array).max().orElse(0)+1];
		int max = -(int)Math.pow(2,31)+1;
		for(int num : array){
			max = Math.max(num,max);
			count[num] += 1;
		} 
		
		for(int i = 0; i < count.length-1; i++){
			count[i+1] = count[i]+count[i+1];
		}

		for(int i = array.length-1; i > 0;i--){
			count[array[i]]--;
			result[count[array[i]]] = array[i];
		}
		return result;
	}

}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Baekjoon_1654 {

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st = new StringTokenizer(in.readLine());
		 
	    int n = Integer.parseInt(st.nextToken());
	    int num = Integer.parseInt(st.nextToken());
		
	    int[] array = new int[n];
		
		for(int i = 0; i < n; i++) {
			array[i] = Integer.parseInt(in.readLine());
		}
		
		Arrays.sort(array);
		
		long right = array[n-1];
		long left = 0;
		long mid = 0;
		long temp = 0;
		
		while(left <= right) {
			mid = right + (left-right)/2;
			
			for(int i = 0; i < n; i++) {
				temp += array[i]/mid;
			}
			
			if (temp >= num) { left = mid+1; }
			else { right = mid-1; }
			temp = 0;
		}
		
		System.out.println(right);
	}

}

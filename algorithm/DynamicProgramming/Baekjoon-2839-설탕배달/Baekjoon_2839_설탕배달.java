import java.util.*;

public class Baekjoon_2839_설탕배달 {
	public static int dynamic(int n,int count) {
		if(n==1 || n==2) {return -1;}
		
		if(n==0) { return count;}
		
		n = n%5 == 0 ? n-5 : n-3;
		
		return dynamic(n,count+1);
		
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		System.out.println(dynamic(n, 0));
		
	}

}

import java.util.*;

public class Baekjoon_2805_나무자르기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int need = sc.nextInt();
        sc.nextLine();

        int left = 0;
        int right = 0;
        int[] tree = new int[n];
        for(int i = 0; i < n; i++){
            tree[i] = sc.nextInt();
            if (tree[i] > right) {right = tree[i];}
        }
        
        Arrays.sort(tree);

        long temp = 0; int mid = 0;
        while(left <= right){
            temp = 0;
            mid = (left+right)/2;
            for(int num : tree){
                if(num > mid ) {temp += num - mid;}
            }
            
            if(temp >= need) {left = mid + 1;}
            else {right = mid-1;}
        }
        System.out.println(right);
    }
}

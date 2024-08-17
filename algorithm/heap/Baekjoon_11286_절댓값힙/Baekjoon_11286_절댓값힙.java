import java.util.*;

public class Baekjoon_11286_절댓값힙 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);   
        PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                if(o1[0] == o2[0]) return o1[1]-o2[1];
                else return Integer.compare(o1[0], o2[0]);
            }
        });
        int n = sc.nextInt();
        sc.nextLine();
        
        for(int i = 0; i < n; i++){
            int input = sc.nextInt();
            sc.nextLine();

            if(input == 0) {
                if(heap.isEmpty()) {System.out.println(0);}
                else {System.out.println(heap.poll()[1]);}
            }
            else {
                heap.offer(new int[]{Math.abs(input),input});
            }
        }      
    }
}

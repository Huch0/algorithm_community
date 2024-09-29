package algorithm.heap.Baekjoon_1927_최소힙;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Baekjoon_1927_최소힙 {
        public static void main(String[] args) throws IOException{
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int input;
        for(int i = 0; i < n; i++){
            input = sc.nextInt();
            sc.nextLine();
            if(input == 0){
                if(maxHeap.isEmpty()) bw.write("0"+"\n");
                else {
                    bw.write(Integer.toString(maxHeap.poll())+"\n");
                }
            }
            else{
                maxHeap.add(input);
            }
            
        }
        bw.flush();
        bw.close();
    }
}

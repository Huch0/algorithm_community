package algorithm.heap.Baekjoon_18870_좌표압축;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.HashMap;

public class Baekjoon_18870_좌표압축 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = Integer.parseInt(st.nextToken());
        }

        int[] sortedArray = array.clone(); // 원래 배열은 출력을 위해 변경되면 안되기 때문에, 정렬된 배열을 위한 배열을 다시 생성.
        Arrays.sort(sortedArray);
        HashMap<Integer,Integer> map = new HashMap<>(); 
        int index = 0;
        int prev = sortedArray[0];

        for(int i = 0; i < sortedArray.length; i++){ 
            if(prev != sortedArray[i]) {index++;} // 정렬된 배열을 순회하며 이전값과 다른 경우에만 index(rank)를 증가.(중복일때 rank를 증가시키지 않기 위한 작업)

            map.put(sortedArray[i],index); // 정렬된 모든 요소를 순회하며 순서대로 요소와 index(rank)를 매핑
            prev = sortedArray[i];
        }   

        for(int i = 0; i < array.length; i++){
            array[i] = map.get(array[i]); // 원래의 배열을 순회하며 순서대로 매핑된 값을 출력
        }
        for (int i : array) {
            bw.write(Integer.toString(i)); bw.write(" ");
        }

        bw.flush();
        bw.close();
    }
}

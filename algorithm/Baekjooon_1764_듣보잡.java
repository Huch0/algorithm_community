package algorithm;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Collections;
import java.io.*;

public class Baekjooon_1764_듣보잡 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] num = new String[2];
        num = br.readLine().split(" ");
        int unheared = Integer.parseInt(num[0]);
        int unseen = Integer.parseInt(num[1]);

        HashSet<String> unhearedSet = new HashSet<String>();
        HashSet<String> unseenSet = new HashSet<String>();

        for(int i = 0; i < unheared; i++){
            unhearedSet.add(br.readLine());
        }

        for(int i = 0; i < unseen; i++){
            unseenSet.add(br.readLine());
        }

        unhearedSet.retainAll(unseenSet);

        ArrayList<String> List = new ArrayList<String>();
        List.addAll(unhearedSet);
        Collections.sort(List);

        System.out.println(List.size());
        
        for(String str : List){
            bw.write(str);
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}

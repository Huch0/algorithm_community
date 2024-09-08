package algorithm.Set.Baekjoon_11723_집합;

import java.util.Set;
import java.util.HashSet;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Baekjoon_11723_집합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        Set<Integer> set = new HashSet<>();
        String[] line;

        for(int i = 0; i < n; i++){
            line = br.readLine().split(" ");

            switch(line[0]){
                case("add") : set.add(Integer.parseInt(line[1])); break;
                case("remove") : set.remove(Integer.parseInt(line[1])); break;
                case("check") : if(set.contains(Integer.parseInt(line[1]))) bw.write(1+"\n"); else bw.write(0+"\n"); break; 
                case("toggle") : if(set.contains(Integer.parseInt(line[1]))) set.remove(Integer.parseInt(line[1])); else set.add(Integer.parseInt(line[1])); break;
                case("all") : set.clear(); for(int j = 1; j < 21; j++) {set.add(j);} break;
                case("empty") : set.clear(); break;
                default : break;
            }
            
        }
        bw.flush();
        bw.close();
    }
}

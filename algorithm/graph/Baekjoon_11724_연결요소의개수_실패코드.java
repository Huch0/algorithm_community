package algorithm.graph;

import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Iterator;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Baekjoon_11724_연결요소의개수_실패코드 {
    static HashMap<Integer,ArrayList<Integer>> map;
    static HashSet<Integer> totalSet;
    static HashSet<Integer> visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        map = new HashMap<>();
        totalSet = new HashSet<>();
        visited = new HashSet<>();
        int result = 0;

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int first = 0;
        int second = 0;

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            first = Integer.parseInt(st.nextToken());
            second = Integer.parseInt(st.nextToken());

            if(!map.containsKey(first)) {map.put(first,new ArrayList<Integer>());}
            if(!map.containsKey(second)) {map.put(second,new ArrayList<Integer>());}
            
            map.get(first).add(second);
            map.get(second).add(first);
        }

        totalSet.addAll(map.keySet());

        Iterator<Integer> it;

        while(!totalSet.isEmpty()){
            it = totalSet.iterator();
            while(it.hasNext()){
                int num = it.next();
                travel(num);
                result++;
                break;
            }
            totalSet.removeAll(visited);
            visited.clear();
        }

        System.out.println(result);
    }

    public static void travel(int key){
        if(visited.contains(key)) return;
        visited.add(key);
        for(int value : map.get(key)){
            travel(value);
        }
    }

}

package algorithm.HashMap.Baekjoon_9375_패션왕신해빈;

import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;

public class Baekjoon_9375_패션왕신해빈 {
    public static void main(String[] args) throws IOException{
        HashMap<String,ArrayList<String>> map = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine());
        
        int n = 0;
        String[] line;
        String key, value;
        int result = 1;
        for(int i = 0; i < testCase; i++){
            n = Integer.parseInt(br.readLine());
            for(int j = 0; j < n; j++){
                line = br.readLine().split(" ");
                key = line[1];
                value = line[0];
                
                if(!map.containsKey(key)) {map.put(key,new ArrayList<>());}
                map.get(key).add(value);
            }

            Iterator mapIterator = map.keySet().iterator();

            while(mapIterator.hasNext()){
                String now = mapIterator.next().toString();
                result *= map.get(now).size()+1;
            }

            System.out.println(result-1);

            map.clear();
            result = 1;
        }
        
        
    }

}

package algorithm.bruteforce;

import java.util.HashSet;

public class 프로그래머스_소수찾기 {
    public static HashSet<Integer> set = new HashSet<>();
    public int solution(String numbers) {
        combination(numbers,"");
        
        int count = 0;
        for(int num : set){
            if(num == 0 || num == 1) continue;
            boolean flag = true;
            for(int i = 2; i <= (int)(Math.sqrt(num));i++){
                if(num%i == 0) {flag = false; break;}
            }
            if(flag) count ++;
        }
        
        return count;
    }
    
    void combination(String numbers, String num){
        if(numbers.length() == 0) {set.add(Integer.parseInt(num)); return;}
            String temp = num;
        for(int i = 0; i < numbers.length();i++){
            num += numbers.charAt(i);
            set.add(Integer.parseInt(num));
            combination(numbers.substring(0,i) + numbers.substring(i+1),num);
            num = temp;
        }
        
        return;
    }
}

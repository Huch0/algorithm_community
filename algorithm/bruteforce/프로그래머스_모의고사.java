package algorithm.bruteforce;

public class 프로그래머스_모의고사 {
    public int[] solution(int[] answers) {
        int[] first = {1,2,3,4,5};
        int[] second = {2,1,2,3,2,4,2,5};
        int[] third = {3,3,1,1,2,2,4,4,5,5};
        
        int[] count = new int[3];
        
        for(int i = 0; i < answers.length; i++){
            if(answers[i] == first[i%first.length]) count[0]++;
            if(answers[i] == second[i%second.length]) count[1]++;
            if(answers[i] == third[i%third.length]) count[2]++;
        }
        
        int max = Math.max(count[0],Math.max(count[1],count[2]));
        int num = 0;
        for(int i = 0; i < count.length; i++){
            if(max == count[i]){num++;}
        }
        
        int[] result = new int[num];
        int index = 0;
        for(int i = 0; i < count.length; i++){
            if(max == count[i]){result[index] = i+1; index++;}
        }
        
        return result;
    }
}

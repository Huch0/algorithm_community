package algorithm.bruteforce;

class 프로그래머스_최소직사각형 {
    public int solution(int[][] sizes) {
        int totalMax = 0;
        boolean isWidth = false;
        boolean isHeight = false;
        
        for(int i = 0; i < sizes.length; i++){
            if(totalMax < sizes[i][0]) {
                totalMax = sizes[i][0];
                isWidth = true;
                isHeight = false;
            }
            else if(totalMax < sizes[i][1]){
                totalMax = sizes[i][1];
                isWidth = false;
                isHeight = true;
            }
        }

        int anotherMax = 0;
        if(isWidth){
            for(int i = 0; i < sizes.length; i++){
                anotherMax = sizes[i][1] > sizes[i][0] ? Math.max(anotherMax,sizes[i][0]) : Math.max(anotherMax,sizes[i][1]);
            }
        }
        else {
            for(int i = 0; i < sizes.length; i++){
                anotherMax = sizes[i][0] > sizes[i][1] ? Math.max(anotherMax,sizes[i][1]) : Math.max(anotherMax,sizes[i][0]);
            }
        }
        
        return totalMax*anotherMax;
    }
}
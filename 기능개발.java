import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int N = progresses.length;
        int[] answer = new int[N];
        
        int p = 0;
        int size = 0;
        while (p < N){
            int job = 100 - progresses[p];
            int time = job / speeds[p] + (job%speeds[p] > 0? 1: 0);
            
            int cnt = 0;
            boolean flag = true;
            for(int i=p; i<N; i++){
                progresses[i] += speeds[i] * time;
                
                if(flag && progresses[i] >= 100){
                    progresses[i] = 100;
                    
                    cnt++;
                    p++;
                }else
                    flag = false;
            }
            
            answer[size++] = cnt;
        }
        
        
        return Arrays.stream(answer).filter(n -> n!=0).toArray();
    }
}

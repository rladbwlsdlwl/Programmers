import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        // min heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int i=0; i<scoville.length; i++)
            pq.offer(scoville[i]);
            
       // 1개일때 또는 최상단 값이 K 이상일때 break
        while(pq.size() >= 2){
            
            int p1 = pq.poll(); int p2 = pq.poll();
            
            if(p1 >= K){
                pq.offer(p1);
                pq.offer(p2);
                break;
            }
            
            int hot = p1+p2*2;
            
            pq.offer(hot);
            
            answer++;
        }
        
        
        if(pq.peek() < K) return -1;
        
        
        return answer;
    }
}

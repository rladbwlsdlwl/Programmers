import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Deque<int[]> q = new ArrayDeque<>();
        
        
        // {우선순위, 인덱스}
        for(int i=0; i<priorities.length; i++)
            q.addLast(new int[]{priorities[i], i});
        
        
        
        while(q.size() > 0){
            // 우선순위가 높은 프로세스 확인
            int[] mx = q.stream()
                .max(Comparator.comparingInt(v -> v[0])).orElse(null);
            
            
            int stopped_idx = -1;
            while(true){
                int[] p = q.removeFirst();
                
                if(p[0] == mx[0]){
                    answer++;
                    stopped_idx = p[1];
                    break;
                }
                
                q.addLast(p);
            }
            
            if(stopped_idx == location)
                return answer;
        }
        
        
        return -1;
    }
}

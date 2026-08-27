import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        // ascending sort
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));
        
        
        int e = -30000;
        for(int[] curr: routes){
            // 끝 값보다 curr의 시작점이 커진 경우 (범위를 벗어남)
            if(e < curr[0]){
                answer++;
                
                e = curr[1];
            }
            
        }
        
        
        return answer;
    }
}

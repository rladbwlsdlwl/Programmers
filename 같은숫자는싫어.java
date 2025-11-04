import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> answer = new ArrayList<>();        
        
        for(int n: arr){
            int size = answer.size();
            if(size > 0 && answer.get(size-1) == n) 
                continue;
            
            answer.add(n);
        }
        
        return answer.stream().mapToInt(Integer:: intValue).toArray();
    }
}

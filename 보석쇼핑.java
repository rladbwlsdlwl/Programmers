import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {};
        
        Set<String> typeSet = new HashSet<>(Arrays.asList(gems));
        Map<String, Integer> typeMap = new HashMap<>();
        
        
        int left = 0, right = 0;
        int length = typeSet.size();
        
        int mn = Integer.MAX_VALUE;
        while(true){
            int currLength = typeMap.size();
            
            if(currLength < length){
                if (right == gems.length) break;
                
                // +1 카운트
                typeMap.put(gems[right], typeMap.getOrDefault(gems[right], 0) + 1);
                
                right++;
                
            }else{
                if(mn > right-left){
                    mn = right - left;
                    answer = new int[]{left+1, right};
                    // System.out.println(answer[0] + ", " + answer[1]);
                }
                
                
                // -1 카운트
                typeMap.put(gems[left], typeMap.get(gems[left]) - 1);
                
                // 없으면 제거
                if(typeMap.get(gems[left]) == 0)
                    typeMap.remove(gems[left]);
                    
                
                left++;
            }
            
        }
        
        
        return answer;
    }
}

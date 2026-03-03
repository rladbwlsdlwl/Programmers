import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Integer> arr = new ArrayList<>();
        
        for(; n>0; n/=10)
            arr.add((int)(n%10));
        
        
        return arr.stream().mapToInt(Integer:: intValue).toArray();
    }
}

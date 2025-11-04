import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stk = new ArrayDeque<>();
        
        
        
        boolean stopped = false;
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c == '('){ 
                stk.addLast(c);
                continue;
            }
            
            
            // 닫힌괄호일경우
            if(stk.size()==0){
                stopped = true;
                break;
            }
            
            
            Character p = stk.removeLast();
            
            
            if(!p.equals('(')){
                stopped = true;
                break;
            }
        }
        
        

        return stk.size() == 0 && !stopped;
    }
}

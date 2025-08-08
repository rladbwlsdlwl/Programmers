import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        int N = s.length();
        for(int i=0; i<N; i++){
            String palindrome = s.substring(i, N) + s.substring(0, i);
            
            boolean stopped = false;
            List<Character> stk = new ArrayList<>();
            for(char pal: palindrome.toCharArray()){ // string to char[] 
                if(pal == '(' || pal == '[' || pal =='{')
                    stk.add(pal);
                else{
                    if(stk.size() == 0){
                        stopped = true;
                        break;
                    }
                    char p = stk.remove(stk.size()-1);
                    
                    if(! (p == '(' && pal == ')' || 
                          p == '{' && pal == '}' || 
                          p == '[' && pal == ']')){
                        stopped = true;
                        break;
                    }
                }
            }
            
            
            if(!stopped && stk.isEmpty())
                answer++;
            
            
            
        }
        
        
        
        return answer;
    }
}

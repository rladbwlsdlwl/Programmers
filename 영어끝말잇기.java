import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Map<String, Boolean> wordlist = new HashMap<>();
        
        
        int cnt = 0;
        boolean isStopped = false;
        String beforeWord = "";
        
        for(String word: words){
            
            if(wordlist.containsKey(word) || beforeWord.length() > 0 && word.charAt(0) != beforeWord.charAt(beforeWord.length() - 1)){
                isStopped = true;
                break;
            }
                
            
            wordlist.put(word, true);
            cnt++;
            
            // 끝말잇기에 해당하는 문자로 시작했는지 비교
            beforeWord = word;
        }
        
        
        int[] ans = new int[2];
        
        if(isStopped)
            ans = new int[]{cnt%n + 1, (cnt/n) + 1};
        else
            ans = new int[]{0, 0};
        
        
        return ans;
    }
}

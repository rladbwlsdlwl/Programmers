import java.util.*;

class Solution {
    public int answer = 0;
    
    public int solution(String[] want, int[] number, String[] discount) {
        
        Map<String, Integer> table = new HashMap<>();
        
        // 필요한 물건 기록
        int i=0;
        for(String food: want)
            table.put(food, number[i++]);
        // 첫날 살 수 있는 물품 소거 
        int size = discount.length;
        for(i=0; i<10 && i<size; i++){
            String key = discount[i];
            if(table.containsKey(key))
                table.put(key, table.get(key)-1);
            
        } 
        
        checkAvailableAllProd(table);
        
        
        // 그 이후는 하루 전날과 다음날만 증감 (누적 계산)
        for(i=1; i<size; i++){
            String key = discount[i-1];
            
            // 전날 할인제품 제거
            if(table.containsKey(key))
                table.put(key, table.get(key)+1);
       
            // 10일 후 할인제품 추가, 인덱스 접근이라 -1 빼주기
            if(i+9 < size){
                key = discount[i+9];
                
                if(table.containsKey(key))
                    table.put(key, table.get(key)-1);
                
            }
            
            // System.out.println(table);
            checkAvailableAllProd(table);
        }
        
        
        return answer;
    }
    
    public void checkAvailableAllProd(Map<String, Integer> table){
        // 모든 제품을 살 수 있는 경우 카운팅
        boolean stopped = false;
        for(String key_: table.keySet()){
            if(table.get(key_) > 0){
                stopped = true;
                break;
            }
        }


        if(!stopped) answer++;
    }
}

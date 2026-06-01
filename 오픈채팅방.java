import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> table = new HashMap<>();
        
        for(String r: record){
            
            String[] rr = r.split(" ");
            
            // 유저 입장 -> 새로운 유저거나 기존 유저 (새로운 유저일 경우를 대비하여 닉네임 기록)
            // 유저 변경 -> 기록되어있는 닉네임 업데이트
            if(rr[0].equals("Enter") || rr[0].equals("Change"))
                table.put(rr[1], rr[2]); // {uid: username}
            
        }
        
        List<String> answer = new ArrayList<>();
        for(String r: record){
            
            String[] rr = r.split(" ");
            String username = table.get(rr[1]);
            
            if(rr[0].equals("Enter"))
                answer.add(username+"님이 들어왔습니다.");
            else if(rr[0].equals("Leave"))
                answer.add(username+"님이 나갔습니다.");
            
            
        }
        
        
        return answer.toArray(String[]:: new);
    }
}

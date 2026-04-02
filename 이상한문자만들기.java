class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        
        int i=0;
        for(char c: s.toCharArray()){
            if(i % 2 == 1 && c >= 'A' && c <= 'Z') // 소문자 치환
                sb.append((char)(c + 32)); // 'a' - 'A' = 32
            else if(i % 2 == 0 && c >= 'a' && c <= 'z') // 대문자 치환
                sb.append((char)(c - 32));
            else
                sb.append(c);
            
            if(c == ' ')
                i = 0;
            else
                i++;
        }
        
        return new String(sb);
    }
}

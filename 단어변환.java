import java.util.*;

record Node(int cnt, String str){}

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int N = target.length();
        int M = words.length;
        
        // {0(count), "hit"(currentStr)}
        ArrayDeque<Node> q = new ArrayDeque<>();
        q.push(new Node(0, begin));
        
        // target으로 변경 불가능한 words 리스트인 경우
        // 재방문시 탐색 중지
        boolean visited[] = new boolean[M];
        
        while(!q.isEmpty()){
            
            Node p = q.poll();
            
            int cnt = p.cnt();
            char[] strList = p.str().toCharArray();
            
            
            if(p.str().equals(target)){
                answer = cnt;
                break;
            }
            
            // 단어 리스트에서 현재 단어와 한 문자만 단어 찾기
            for(int i=0; i<M; i++){
                
                int cmp = 0;
                char[] word = words[i].toCharArray();
                for(int j=0; j<N; j++){
                    if(strList[j] != word[j])
                        cmp++;
                }
                
                
                // 이미 방문한 노드는 재방문 불가 (그래프 사이클 차단)
                if(cmp == 1 && !visited[i]){
                    q.push(new Node(cnt+1, words[i]));
                    visited[i] = true;
                }
            }
            
            
        }
            
        
            
        return answer;
    }
}

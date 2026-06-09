import java.util.*;


class Solution {
    private int r;
    private int c;
    
    private int[] dy = {-1, 0, 1, 0};
    private int[] dx = {0, 1, 0, -1};
    
    private int dfs(int y, int x, char[][] maze){
        int ans = 0;
        
        
        for(int i=0; i<4; i++){
            int movey = y + dy[i], movex = x + dx[i];
            
            if(movey < 0 || movey >= r || movex < 0 || movex >= c)
                continue;
            
            if(maze[movey][movex] != 'X'){
                int tmp = maze[movey][movex] - '0';
                maze[movey][movex] = 'X';
                
                ans += dfs(movey, movex, maze) + tmp;
            }
        }
        
        
        return ans;
        
        
    }
    
    public int[] solution(String[] maps) {
        r = maps.length; c = maps[0].length();
        
        // init
        char[][] maze = new char[r][c];
        for(int i=0; i<r; i++)
            maze[i] = maps[i].toCharArray();
        
        
        // dfs
        List<Integer> answer = new ArrayList<>();
        for(int i=0; i<r; i++){   
            for(int j=0; j<c; j++){
                if(maze[i][j] != 'X'){
                    int tmp = maze[i][j] - '0';
                    maze[i][j] = 'X';
                    
                    answer.add(dfs(i, j, maze) + tmp);
                }
            }
        }
        
        
        int[] ans = answer.stream().mapToInt(Integer:: intValue).toArray();
        
        Arrays.sort(ans);
        
        return ans.length == 0 ? new int[]{-1} : ans;
    }
}

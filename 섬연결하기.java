import java.util.*;


record Node(int w, int n){}


class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        
        List<List<Node>> graph = new ArrayList<>();
        
        // initialize
        for(int i=0; i<n; i++)
            graph.add(new ArrayList<>());
        
        
        for(int[] cost: costs){
            graph.get(cost[0]).add(new Node(cost[2], cost[1])); // weight, node
            graph.get(cost[1]).add(new Node(cost[2], cost[0])); // weight, node
        }
        
        
        // dijkstra
        // min heap (weight 기준 ascending sort)
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.w() - b.w());
        pq.offer(new Node(0, 0));
        
        
        int cnt = 0;
        
        
        boolean visited[] = new boolean[n];
        while(cnt < n){
            
            Node p = pq.poll();
            int w = p.w();
            int node = p.n();
            
            if(visited[node])
                continue;
            
            
            answer += w;
            cnt++;
            visited[node] = true;
            
            for(Node child: graph.get(node)){
                int weight = child.w();
                int goal = child.n();
                
                if(!visited[goal])
                    pq.offer(new Node(weight, goal));
            }
            
        }
        
        
        
        return answer;
    }
}

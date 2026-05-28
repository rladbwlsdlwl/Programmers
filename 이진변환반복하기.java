class Solution {
    public int[] solution(String s) {
        
        int count = 0;
        int zero_count = 0;
        while(!s.equals("1")){
            // remove 0
            
            int one_count = 0;
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i) == '1')
                    one_count++;
                else
                    zero_count++;
            }
            
            s = Integer.toBinaryString(one_count);
            count++;
        }
        
        
        return new int[]{count, zero_count};
    }
}

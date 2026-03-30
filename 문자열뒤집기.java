class Solution {
    public String solution(String my_string, int s, int e) {
        
//         char[] str = my_string.toCharArray();
        
        
//         while(s<e){
//             char temp = str[s];
//             str[s++] = str[e];
//             str[e--] = temp;
//         }
        
//         return new String(str);
        
        
        // reverse 와 substring 활용하기
        StringBuilder str = new StringBuilder(my_string.substring(s, e+1));
        
        str.reverse();
            
        return my_string.substring(0, s) + str + my_string.substring(e+1);
    }
}

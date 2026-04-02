import java.util.*;

class Solution {
    public int solution(String s) {
//         Map<String, String> table = new HashMap<>();
        
//         table.put("zero", "0");
//         table.put("one", "1");
//         table.put("two", "2");
//         table.put("three", "3");
//         table.put("four", "4");
//         table.put("five", "5");
//         table.put("six", "6");
//         table.put("seven", "7");
//         table.put("eight", "8");
//         table.put("nine", "9");
        
//         for(String key: table.keySet())
//             s = s.replaceAll(key, table.get(key));
        
//         return Integer.parseInt(s);
        
        
        String[] numberlist = {"zero", "one", "two", "three", "four", 
                               "five", "six", "seven", "eight", "nine"};
        
        
        for(int i = 0; i < 10; i++)
            s = s.replaceAll(numberlist[i], "" + i);
        
        
        return Integer.parseInt(s);
    }
}

/**387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
*/

//solution 1: map to store the position of each characters
// time complexicity: O(n) 
//space complexity: O(n)
class Solution {
    public int firstUniqChar(String s) {
        
        if(s == null || s.length() == 0){
            return -1;
        }
        
        //key: letter, val: pos( if -1: repeated)
        Map<Character, Integer> map = new HashMap<>();
        Integer min = null;
        
        
        for(int i = 0 ; i< s.length(); i++){
            Character c = s.charAt(i);
            if(map.containsKey(c)){
                map.put(c, -1);
            }else{
                map.put(c, i);
            }
        }
        
        for(Character c: map.keySet()){
            int pos = map.get(c);
            if(pos == -1){
                continue;
            }else{
                if(min == null){
                    min = pos;
                }else{
                    min = Math.min(min, pos);
                }
            }
        }
        
        if(min == null){
            min = -1;
        }
        
        return min;
        
    }
}

//solution 2, using int characters table to store the count of each characters(lower case in this question)
// time complexicity: O(n) 
//space complexity: O(1)
class Solution {
    public int firstUniqChar(String s) {
        if(s == null || s.length() == 0){
            return -1;
        }
        int letters[] = new int[26];
        
        for(char c: s.toCharArray()){
            letters[c-'a']++;
        }
        
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(letters[c-'a'] == 1){
                return i;
            }
        }
        
        return -1;
    }
}


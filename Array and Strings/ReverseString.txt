/**
344. Reverse String
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

focus: remember to left++ and right-- to avoid infinite loop;
**/


class Solution {
    public String reverseString(String s) {
        if(s == null || s.length() < 2){
            return s;
        }
        
        char chars[]= s.toCharArray();
        int left = 0, right = s.length()-1;
        while(left < right){
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
        
        return new String(chars); 
    }
}
/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

company: amazon
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int index=0; index < nums.length; index++){
            int num1 = nums[index];
            
            int num0 = target - num1;
            
            if(map.containsKey(num0)){
                int indexOfNum0 = map.get(num0); 
                return new int[]{indexOfNum0, index};
            }else{
                map.put(nums[index], index);    
            }
        }
        
        return null;
        
    }
}
 

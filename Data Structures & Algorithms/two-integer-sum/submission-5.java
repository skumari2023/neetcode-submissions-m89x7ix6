class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        for(int x = 0; x < nums.length; x++)
        {
            for (int y = x + 1; y < nums.length; y++)
            {
                if(nums[x]+ nums[y] == target)
                {
                   //System.out.print("[" + x + "," + y + "]"); -> need a return statement for int
                   return new int [] {x,y};
                }
            }
        }
        //don't forget the return statement if the cases were not true
        return new int [] {};
    }
}

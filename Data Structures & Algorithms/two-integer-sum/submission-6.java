class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        HashMap <Integer,Integer>  seen = new HashMap <>();
        for (int x = 0; x < nums.length; x++)
        {
            int value = target - nums[x];
            if (seen.containsKey(value))
            {
                if ( x < seen.get(value))
                {
                    return new int [] {x,seen.get(value)};
                }
                else
                {
                    return new int [] {seen.get(value), x};
                }
            }
            seen.put(nums[x],x);
        }
        return new int [] {};

    }
}

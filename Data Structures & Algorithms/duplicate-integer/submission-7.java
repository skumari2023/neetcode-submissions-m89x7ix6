class Solution 
{
    public boolean hasDuplicate(int[] nums) 
    {
        HashSet <Integer> seen = new HashSet<>();
        for (int numbers : nums)
        {
            if (seen.contains(numbers))
            {
                return true;
            }
            seen.add(numbers);
        }
        return false;
    }

}

class Solution {
    public boolean isAnagram(String s, String t) 
    {
        if (s.length()!= t.length())
        {
            return false;
        }

        HashMap <Character, Integer> anagram = new HashMap <>();

        for (char character: s.toCharArray())
        {
            //getOrDefault gives the default frequency of 0 if it doesn't exist
            anagram.put(character, anagram.getOrDefault(character,0)+ 1);
        }

        for (char chars : t.toCharArray())
        {
            if(!anagram.containsKey(chars))
            {
                return false;
            }

            //getting the frequency of each of the characters to 0 
            anagram.put(chars, anagram.get(chars)-1);

            if(anagram.get(chars)<0)
            {
                return false; 
            }
        }
        return true;
    }
}

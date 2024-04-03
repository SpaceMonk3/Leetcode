class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        int tempCounter = 0;
        HashMap<Character, Integer> used = new HashMap<>();

        for(int sw = 0; sw < s.length();  sw++){
            for(int i = sw; i < s.length(); ){
                if(used.get(s.charAt(i)) == null){
                    used.put(s.charAt(i), 1);
                    tempCounter++;
                    i++; 

                    if(tempCounter > longest){
                        longest = tempCounter;
                    }
                }
                else{
                    tempCounter = 0;
                    used.clear();
                    break;
                }
            } 
        }

        return longest; 
    }
}

//keep track of string length and compare with previous ones
//keep track of used characters (using ascii code)
//loop linearly

//dvdf move one position to the right everytime a repeating character is noticed
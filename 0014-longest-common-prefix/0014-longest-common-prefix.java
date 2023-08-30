class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = "";
        if(strs.length<2){
            return strs[0];
        }

        int minStringLength = minStringLength(strs);

        for(int i=0; i<minStringLength; i++){
            for(int j=1; j<strs.length; j++){
                if(strs[j].charAt(i) != strs[0].charAt(i)){
                    return result;
                }
            }
            result += strs[0].charAt(i);
        }
        return result;
    }

    // get minimum string length inside array of strings
    public int minStringLength(String[] strs){
        int minLength = strs[0].length();
        for(int i=0; i<strs.length; i++){
            if(strs[i].length() < minLength){
                minLength = strs[i].length();
            }
        }
        return minLength;
    }

}
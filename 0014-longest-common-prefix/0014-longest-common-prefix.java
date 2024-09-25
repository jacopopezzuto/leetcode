class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length==1) return strs[0];
        String result = strs[0];
        for(int i=1; i<strs.length; i++){
            result = findCommonPrefix(result,strs[i]);
        }
        return result;
    }

    public String findCommonPrefix(String str1, String str2){
        int minLength = str1.length()<str2.length() ? str1.length() : str2.length();
        for(int i=0; i<minLength; i++){
            if(str1.charAt(i)!=str2.charAt(i)){
                return str1.substring(0,i);
            }
        }
        return str1.substring(0,minLength);
    }
}
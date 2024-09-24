class Solution {
    public char repeatedCharacter(String s) {
        int[] alphabet = new int[26];
        for(int i=0; i<s.length(); i++){
            if(alphabet[s.charAt(i)-'a']>0){
                return s.charAt(i);
            }else{
                alphabet[s.charAt(i)-'a']++;
            }
        }
        return ' ';
    }
}
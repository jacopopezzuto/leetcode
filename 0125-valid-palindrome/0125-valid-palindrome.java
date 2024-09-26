class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder filtered = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            if((s.charAt(i) >= 'a' && s.charAt(i) <= 'z') || (s.charAt(i) >= '0' && s.charAt(i) <= '9')){
               filtered.append(s.charAt(i));
            }
        }
        int j=filtered.length()-1;
        for(int i=0; i<filtered.length()/2; i++){
            if(filtered.charAt(i)!=filtered.charAt(j)){
                return false;
            }
            j--;
        }
        return true;
    }
}
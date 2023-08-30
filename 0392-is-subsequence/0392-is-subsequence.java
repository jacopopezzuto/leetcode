class Solution {
    public boolean isSubsequence(String s, String t) {
        int v=-1;
        int result=0;
        for(int i=0; i<s.length();i++){
            for(int j=v+1; j<t.length();j++){
                if(s.charAt(i)==t.charAt(j)){
                    v=j;
                    ++result;
                    break;
                }
            }
        }
        return result==s.length();
    }
}
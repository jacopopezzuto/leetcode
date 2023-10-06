class Solution {
    public boolean isPalindrome(int x) {
        int z=x;
        int y=0;
        if(x<0) return false;
        while(x>0){
            y*=10;
            y+=x%10;
            x/=10;
        }
        return z==y;
    }
}
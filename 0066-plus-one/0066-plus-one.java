class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for(int i=n-1; i>-1; i--){
            digits[i]= (digits[i]+1)%10;
            if(digits[i]!=0){
                return digits;
            }
        }
        int[] result = new int[n+1];
        result[0]=1;
        return result;
    }
}
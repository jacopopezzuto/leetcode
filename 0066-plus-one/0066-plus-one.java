class Solution {
    public int[] plusOne(int[] digits) {
       for(int i=digits.length-1; i>-1; i--){
           digits[i] = (digits[i]+1) % 10;
           if(digits[i]!=0){
               return digits;
           }
       }
        int[] result = new int[digits.length+1];
        result[0] = 1;
        return result;
    }
}
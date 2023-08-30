class Solution {
    public int[] replaceElements(int[] arr) {
        for(int i=0; i<arr.length; i++){
            arr[i]=greatestFromRight(arr,i+1);
        }
        return arr;
    }
    public int greatestFromRight(int[] arr, int start){
        if(start>=arr.length) return -1;
        int maxElem = arr[start];
        for(int i=start; i<arr.length; i++){
            maxElem = maxElem > arr[i] ? maxElem : arr[i];
        } 
        return maxElem;
    }
}
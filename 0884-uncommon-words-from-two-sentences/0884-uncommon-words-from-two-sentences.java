class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> map = new HashMap<>();
        String result = s1 + " " + s2;
        for(String word: result.split(" ")){
            if(map.containsKey(word)){
                map.replace(word,map.get(word)+1);
            }else{
                map.put(word,1);
            }
        }
        ArrayList<String> output = new ArrayList<>();
        for(Map.Entry<String, Integer> entry : map.entrySet()){
            if(entry.getValue()==1){
                output.add(entry.getKey());
            }
        }
        return output.toArray(new String[0]);
    }
}
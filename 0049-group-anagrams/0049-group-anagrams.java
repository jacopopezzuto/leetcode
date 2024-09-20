class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(int i=0; i<strs.length; i++){
            char[] characters = strs[i].toCharArray();
            Arrays.sort(characters);
            String sortedString = new String(characters);
            List<String> item = map.get(sortedString);
            if(item!=null){
                item.add(strs[i]);
                map.replace(new String(characters), item);
            }else{
                List<String> newItem = new ArrayList<>();
                newItem.add(strs[i]);
                map.put(String.valueOf(characters), newItem);
            }
        }
        List<List<String>> result = new ArrayList<>();
        for(Map.Entry<String, List<String>> entry : map.entrySet()){
            result.add(entry.getValue());
        }
        return result;
    }
}
class Solution {
    public int lengthOfLastWord(String s) {
        int result = 0;
        s = s.trim();
        List<String> list = Arrays.asList(s.split(" "));
        return list.get(list.size()-1).length();
    }
}
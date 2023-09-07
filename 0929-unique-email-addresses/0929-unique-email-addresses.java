class Solution {
    public int numUniqueEmails(String[] emails) {
        HashSet<String> mapDifferentEmail = new HashSet<>();
        for(int i=0; i<emails.length; i++){
            mapDifferentEmail.add(sanitizeEmail(emails[i]));
        }
        return mapDifferentEmail.size();
    }
    
    String sanitizeEmail(String email){
        String result="";
        boolean ignore=false;
        for(int i=0; email.charAt(i)!='@'; i++){
            if(email.charAt(i)=='+') ignore=true;
            if(email.charAt(i)!='.' && ignore==false) result+=email.charAt(i);
            if(email.charAt(i+1)=='@'){
                result+=email.substring(i+1,email.length());
            }
        }
        return result;
    }
}
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result=set()
        for email in emails:
            email=email.split("@")
            local_name="".join(email[0].split("+")[0].split("."))
            domain_name=email[1]
            email=f"{local_name}@{domain_name}"
            result.add(email)
        return len(result)
            